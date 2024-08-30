from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_name = Column(String(100), nullable=True)  # Nullable
    fermi_job_id = Column(String(50), nullable=True)  # Nullable
    user_id = Column(String(100), nullable=True)  # Nullable
    created_at = Column(DateTime, default=datetime.now)

    # Relationships
    main_stats = relationship("MainStats", back_populates="job")
    runtime_analysis = relationship("RuntimeAnalysis", back_populates="job")
    geometric_analysis = relationship("GeometricAnalysis", back_populates="job")
    statistical_analysis = relationship("StatisticalAnalysis", back_populates="job")

    # Indexes to optimize querying by job_name, fermi_job_id, or user_id
    __table_args__ = (
        Index('idx_job_name', 'job_name'),
        Index('idx_fermi_job_id', 'fermi_job_id'),
        Index('idx_user_id', 'user_id'),
    )

class MainStats(Base):
    __tablename__ = 'main_stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='SET NULL'), nullable=True)
    property = Column(String(100), nullable=False)
    value = Column(String(100))
    job = relationship("Job", back_populates="main_stats")

class RuntimeAnalysis(Base):
    __tablename__ = 'runtime_analysis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='SET NULL'), nullable=True)
    property = Column(String(100), nullable=False)
    value = Column(String(100))
    job = relationship("Job", back_populates="runtime_analysis")

class GeometricAnalysis(Base):
    __tablename__ = 'geometric_analysis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='SET NULL'), nullable=True)
    property = Column(String(100), nullable=False)
    value = Column(String(100))
    job = relationship("Job", back_populates="geometric_analysis")

class StatisticalAnalysis(Base):
    __tablename__ = 'statistical_analysis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='SET NULL'), nullable=True)
    set_id = Column(Integer, nullable=False)
    property = Column(String(100), nullable=False)
    value = Column(String(100))
    job = relationship("Job", back_populates="statistical_analysis")

# Database setup
def setup_database():
    engine = None
    try:
        engine = create_engine('mysql+pymysql://d2s:d2s_1234@localhost:3307/emumbaqor')
    except Exception as e:
        print("Couldn't connect to the database. Please check your connection string.", e)
        return
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def get_session():
    return setup_database()

def insert_job(session, job_data):
    # Check if a job with the same fermi_job_id already exists
    job = session.query(Job).filter_by(fermi_job_id=job_data['fermi_job_id']).one_or_none()
    
    if job is None:
        # No existing job found, create a new one
        job = Job(
            fermi_job_id=job_data['fermi_job_id'],
            user_id=job_data['user_id'],
            job_name=job_data['job_name']
        )
        session.add(job)
        session.commit()
    else:
        # Existing job found, update it
        job.user_id = job_data['user_id']
        job.job_name = job_data['job_name']
        session.commit()

    return job.id

def insert_main_stats(session, job_id, data):
    # Clear existing entries and insert new data for Main Stats
    session.query(MainStats).filter_by(job_id=job_id).delete()
    for key, value in data.items():
        main_stats = MainStats(job_id=job_id, property=key, value=value)
        session.add(main_stats)
    session.commit()

def insert_runtimeanalysis_stats(session, job_id, data):
    # Clear existing entries and insert new data for Runtime Analysis
    session.query(RuntimeAnalysis).filter_by(job_id=job_id).delete()
    for key, value in data.items():
        rta_stats = RuntimeAnalysis(job_id=job_id, property=key, value=value)
        session.add(rta_stats)
    session.commit()

def insert_geometricanalysis_stats(session, job_id, data):
    # Clear existing entries and insert new data for Geometric Analysis
    session.query(GeometricAnalysis).filter_by(job_id=job_id).delete()
    for key, value in data.items():
        ga_stats = GeometricAnalysis(job_id=job_id, property=key, value=value)
        session.add(ga_stats)
    session.commit()

def insert_statistical_analysis_stats(session, job_id, data):
    # Clear existing entries and insert new data for Statistical Analysis
    session.query(StatisticalAnalysis).filter_by(job_id=job_id).delete()
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
def main():
    session = get_session()

    # Parse the fermi.txt file
    fermi_file_path = os.path.expanduser('./fermicopy.txt')
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