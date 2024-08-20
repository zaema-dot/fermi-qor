from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
import os

Base = declarative_base()

class MainStats(Base):
    __tablename__ = 'main_stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fermi_id = Column(Integer)
    checker_id = Column(Integer)
    gpu = Column(Integer)
    expect_run_time_50_gpu = Column(Float)
    expect_run_time_1_gpu = Column(Float)
    user = Column(String(50))
    name = Column(String(50))
    max_err_per_partion = Column(String(50))
    total_errors = Column(String(50))
    design_size = Column(String(50))
    mask_file_size = Column(Float)
    recipe_name = Column(String(50))
    mbf_size = Column(Float)
    pdose_simulation_size = Column(Float)
    pdefocus_simulation_size = Column(Float)
    ndefocus_simulation_size = Column(Float)
    nominal_simulation_size = Column(Float)
    ndose_simulation_size = Column(Float)
    target_file_size = Column(Float)
    machine_name = Column(String(50))
    run_date_time = Column(DateTime)
    revision_branch = Column(String(100))
    revision_commit = Column(String(100))
    revision_date = Column(DateTime)
    fermi_job_name = Column(String(50))
    tmod_name = Column(String(100))
    process_condition = Column(String(100))
    partition = Column(String(50))
    grid = Column(Integer)
    optimizer_iterations = Column(String(50))
    force_flag = Column(String(50))
    force_screenshot = Column(String(50))
    mpi_retry_count = Column(String(50))
    num_qtm3_iterations = Column(String(50))
    num_qtm4_iterations = Column(String(50))
    num_qtm5_iterations = Column(String(50))
    mask_num_deleted_shapes = Column(String(50))
    mask_num_upsized_shapes = Column(String(50))
    num_pixel_corrections = Column(String(50))
    num_part_corrections = Column(String(50))
    delete_mask_polygon_count = Column(String(50))
    delete_mask_polygon_max = Column(String(50))
    delete_mask_polygon_min = Column(String(50))
    upsizing_mask_polygon_count = Column(String(50))
    upsizing_mask_polygon_max = Column(String(50))
    upsizing_mask_polygon_min = Column(String(50))
    number_of_optimized_partitions = Column(Integer)
    total_number_of_partitions = Column(Integer)
    parsing_time = Column(String(50))

class RuntimeAnalysis(Base):
    __tablename__ = 'runtime_analysis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    target_prep_runtime = Column(Float)
    ctm_fg = Column(Float)
    qtm_fg = Column(Float)
    ctm_prep = Column(Float)
    qtm0_prep = Column(Float)
    qtm1_prep = Column(Float)
    qtm2_prep = Column(Float)
    qtm3_prep = Column(Float)
    qtm4_prep = Column(Float)
    qtm5_prep = Column(Float)
    qtm0_total = Column(Float)
    qtm1_total = Column(Float)
    qtm2_total = Column(Float)
    qtm3_total = Column(Float)
    qtm4_total = Column(Float)
    qtm5_total = Column(Float)
    ctm_exec_time = Column(Float)
    qtm_exec_time = Column(Float)
    total_prediction_time = Column(Float)
    mrc1_time = Column(Float)
    mrc2_time = Column(Float)
    mbf_exec_time = Column(Float)
    postprocess_exec_time = Column(Float)
    total_fermi_runtime = Column(Float)
    the_checker_runtime = Column(String(50))

class GeometricAnalysis(Base):
    __tablename__ = 'geometric_analysis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    mrc_area_count = Column(Integer)
    mrc_area_max_value = Column(Float)
    mrc_area_min_value = Column(Float)
    mrc_area_marker_x = Column(Integer)
    mrc_area_marker_y = Column(Integer)
    imrcfix_max_correction_max_value = Column(Float)
    imrcfix_total_number_of_fixed_mrc_width_errors_count = Column(Integer)
    imrcfix_total_number_of_partially_fixed_mrc_width_errors_count = Column(Integer)
    imrcfix_the_worst_width_error_overall_max_value = Column(Float)
    imrcfix_total_number_of_fixed_mrc_spacing_errors_count = Column(Integer)
    imrcfix_total_number_of_partially_fixed_mrc_spacing_errors_count = Column(Integer)
    imrcfix_the_worst_spacing_error_overall_max_value = Column(Float)
    imrcfix_total_number_of_unimproved_mrc_errors_count = Column(Integer)
    high_curvature_internal_checking_setting = Column(Integer)
    high_curvature_external_checking_setting = Column(Integer)
    mrc_area_setting = Column(Float)
    mrc_spacing_setting = Column(Float)
    mrc_width_setting = Column(Float)
    mrc_width_count = Column(Integer)
    mrc_width_max_value = Column(Float)
    mrc_width_min_value = Column(Float)
    mrc_width_marker_x = Column(Integer)
    mrc_width_marker_y = Column(Integer)
    mrc_spacing_count = Column(Integer)
    mrc_spacing_max_value = Column(Float)
    mrc_spacing_min_value = Column(Float)
    mrc_spacing_marker_x = Column(Integer)
    mrc_spacing_marker_y = Column(Integer)
    high_curvature_internal_checking_count = Column(Integer)
    high_curvature_internal_checking_max_value = Column(Float)
    high_curvature_internal_checking_min_value = Column(Float)
    high_curvature_internal_checking_marker_x = Column(Integer)
    high_curvature_internal_checking_marker_y = Column(Integer)
    high_curvature_external_checking_count = Column(Integer)
    high_curvature_external_checking_max_value = Column(Float)
    high_curvature_external_checking_min_value = Column(Float)
    high_curvature_external_checking_marker_x = Column(Integer)
    high_curvature_external_checking_marker_y = Column(Integer)
    xor_error_of_nominal_contour_greater_than_15_count = Column(Integer)
    xor_error_of_nominal_contour_greater_than_15_max_value = Column(Float)
    xor_error_of_nominal_contour_greater_than_15_min_value = Column(Float)
    xor_error_of_nominal_contour_greater_than_15_marker_x = Column(Integer)
    xor_error_of_nominal_contour_greater_than_15_marker_y = Column(Integer)
    xor_error_of_negative_dose_greater_than_15_count = Column(Integer)
    xor_error_of_negative_dose_greater_than_15_max_value = Column(Float)
    xor_error_of_negative_dose_greater_than_15_min_value = Column(Float)
    xor_error_of_negative_dose_greater_than_15_marker_x = Column(Integer)
    xor_error_of_negative_dose_greater_than_15_marker_y = Column(Integer)
    xor_error_of_positive_dose_greater_than_15_count = Column(Integer)
    xor_error_of_positive_dose_greater_than_15_max_value = Column(Float)
    xor_error_of_positive_dose_greater_than_15_min_value = Column(Float)
    xor_error_of_positive_dose_greater_than_15_marker_x = Column(Integer)
    xor_error_of_positive_dose_greater_than_15_marker_y = Column(Integer)
    xor_error_of_negative_defocus_greater_than_15_count = Column(Integer)
    xor_error_of_negative_defocus_greater_than_15_max_value = Column(Float)
    xor_error_of_negative_defocus_greater_than_15_min_value = Column(Float)
    xor_error_of_negative_defocus_greater_than_15_marker_x = Column(Integer)
    xor_error_of_negative_defocus_greater_than_15_marker_y = Column(Integer)
    xor_error_of_positive_defocus_greater_than_15_count = Column(Integer)
    xor_error_of_positive_defocus_greater_than_15_max_value = Column(Float)
    xor_error_of_positive_defocus_greater_than_15_min_value = Column(Float)
    xor_error_of_positive_defocus_greater_than_15_marker_x = Column(Integer)
    xor_error_of_positive_defocus_greater_than_15_marker_y = Column(Integer)


class StatisticalAnalysis(Base):
    __tablename__ = 'statistical_analysis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    set_id = Column(Integer, nullable=False)  # This will be used to differentiate sets
    mean_fermi = Column(Float)
    std_fermi = Column(Float)
    max_fermi = Column(Float)
    count_fermi = Column(Integer)
    marker_x_fermi = Column(Float)
    marker_y_fermi = Column(Float)
    
# Database setup
def setup_database():
    # Replace with your actual MySQL connection details
    engine = create_engine('mysql+pymysql://d2s:d2s_1234@localhost/emumbaqor')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Insert data into the database
def insert_main_stats(session, data):
    main_stats = MainStats(**data)
    session.add(main_stats)
    session.commit()

def insert_runtimeanalysis_stats(session, data):
    rta_stats = RuntimeAnalysis(**data)
    session.add(rta_stats)
    session.commit()


def insert_geometricanalysis_stats(session, data):
    ga_stats = GeometricAnalysis(**data)
    session.add(ga_stats)
    session.commit()

def insert_statistical_analysis_stats(session, data):
    sa_stats = StatisticalAnalysis(**data)
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
        'statistical_analysis': statistical_analysis
    }



def main():
    session = setup_database()

    # Parse the fermi.txt file
    fermi_file_path = os.path.expanduser('~/Documents/rsync/11610/qor/fermi.txt')
    parsed_data = parse_fermi_txt(fermi_file_path)

    # Debug: Print parsed data before insertion
    print("Parsed Main Stats:", parsed_data['main_stats'])
    print("Parsed Runtime Analysis Stats:", parsed_data['runtime_analysis_stats'])
    print("Parsed Geometric Analysis Stats:", parsed_data['geometric_analysis_stats'])
    print("Parsed Statistical Analysis Sets:", parsed_data['statistical_analysis'])

    # Insert data into the database
    insert_main_stats(session, parsed_data['main_stats'])
    insert_runtimeanalysis_stats(session, parsed_data['runtime_analysis_stats'])
    insert_geometricanalysis_stats(session, parsed_data['geometric_analysis_stats'])

    # Insert each statistical set with its set_id
    for stat_set in parsed_data['statistical_analysis']:
        insert_statistical_analysis_stats(session, stat_set)

    print("Data successfully inserted into the database.")

if __name__ == "__main__":
    main()
