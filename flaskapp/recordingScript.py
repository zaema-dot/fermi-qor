from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Import the schema from createDB.py
from createDB import Job, MainStats, RuntimeAnalysis, GeometricAnalysis, StatisticalAnalysis, setup_database

# Database setup (reusing the session creation function from createDB.py)
def get_session():
    return setup_database()

# Insert data into the database
def insert_main_stats(session, job_id, data):
    for key, value in data.items():
        main_stats = MainStats(job_id=job_id, property=key, value=value)
        session.add(main_stats)
    session.commit()

def insert_runtimeanalysis_stats(session, job_id, data):
    for key, value in data.items():
        rta_stats = RuntimeAnalysis(job_id=job_id, property=key, value=value)
        session.add(rta_stats)
    session.commit()

def insert_geometricanalysis_stats(session, job_id, data):
    for key, value in data.items():
        ga_stats = GeometricAnalysis(job_id=job_id, property=key, value=value)
        session.add(ga_stats)
    session.commit()

def insert_statistical_analysis_stats(session, job_id, data):
    set_id = data.pop('set_id')
    for key, value in data.items():
        sa_stats = StatisticalAnalysis(job_id=job_id, set_id=set_id, property=key, value=value)
        session.add(sa_stats)
    session.commit()

def parse_fermi_txt(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    # Dictionaries to hold the parsed data for each section
    main_stats = {}
    runtime_analysis_stats = {}
    geometric_analysis_stats = {}
    statistical_analysis = []

    current_section = None
    current_statistical_set = {}
    set_id = None

    for line in content:
        line = line.strip()

        # Detect the section we are in
        if line.startswith("[Main_Stats]"):
            current_section = 'main_stats'
        elif line.startswith("[Runtime_Analysis_Stats]"):
            current_section = 'runtime_analysis'
        elif line.startswith("[Geometric_Analysis_Stats_Fermi]"):
            current_section = 'geometric_analysis'
        elif line.startswith("[Statistical_Analysis]"):
            current_section = 'statistical_analysis'
            current_statistical_set = {}
        elif ":" in line:
            key, value = line.split(":", 1)
            key, value = key.strip(), value.strip()

            # Assign values based on the current section
            if "Set" in key:
                # Extract the set number
                set_id = int(key.split(" ")[1])
            elif current_section == 'main_stats':
                main_stats[key] = value if value != "None" else None
            elif current_section == 'runtime_analysis':
                runtime_analysis_stats[key] = value if value != "None" else None
            elif current_section == 'geometric_analysis':
                geometric_analysis_stats[key] = value if value != "None" else None
            elif current_section == 'statistical_analysis':
                current_statistical_set[key] = value if value != "None" else None

        # If we've finished a statistical set, add it to the list
        if current_section == 'statistical_analysis' and len(current_statistical_set) == 6:
            current_statistical_set['set_id'] = set_id
            statistical_analysis.append(current_statistical_set)
            current_statistical_set = {}

    # Return the parsed data as a dictionary
    return {
        'main_stats': main_stats,
        'runtime_analysis_stats': runtime_analysis_stats,
        'geometric_analysis_stats': geometric_analysis_stats,
        'statistical_analysis': statistical_analysis,
        'job_data': {
            'fermi_job_id': main_stats.get('fermi_id'),
            'user_id': main_stats.get('user'),
            'job_name': main_stats.get('name')
        }
    }

def insert_job(session, job_data):
    job = Job(
        fermi_job_id=job_data['fermi_job_id'],
        user_id=job_data['user_id'],
        job_name=job_data['job_name']
    )
    session.add(job)
    session.commit()
    return job.id

def main():
    session = get_session()

    # Parse the fermi.txt file
    fermi_file_path = os.path.expanduser('./fermi.txt')
    parsed_data = parse_fermi_txt(fermi_file_path)

    # Insert job data and get job_id
    job_id = insert_job(session, parsed_data['job_data'])

    # Insert stats data into the respective tables
    insert_main_stats(session, job_id, parsed_data['main_stats'])
    insert_runtimeanalysis_stats(session, job_id, parsed_data['runtime_analysis_stats'])
    insert_geometricanalysis_stats(session, job_id, parsed_data['geometric_analysis_stats'])

    # Insert each statistical set with its set_id
    for stat_set in parsed_data['statistical_analysis']:
        insert_statistical_analysis_stats(session, job_id, stat_set)

    print("Data successfully inserted into the database.")

if __name__ == "__main__":
    main()
