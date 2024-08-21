import argparse
import os
import copy
import logging

# Create Dictionary keys for each set of statistics

main_keys = [
    "fermi_id",
    "checker_id",
    "gpu",
    "expect_run_time_50_gpu",
    "expect_run_time_1_gpu",
    "user",
    "name",
    "max_err_per_partion",
    "total_errors",
    "design_size",
    "mask_file_size",
    "recipe_name",
    "mbf_size",
    "pdose_simulation_size",
    "pdefocus_simulation_size",
    "ndefocus_simulation_size",
    "nominal_simulation_size",
    "ndose_simulation_size",
    "target_file_size",
    "machine_name",
    "run_date_time",
    "revision_branch",
    "revision_commit",
    "revision_date",
    "fermi_job_name",
    "tmod_name",
    "process_condition",
    "partition",
    "grid",
    "optimizer_iterations",
    "force_flag",
    "force_screenshot",
    "mpi_retry_count",
    "num_qtm3_iterations",
    "num_qtm4_iterations",
    "num_qtm5_iterations",
    "mask_num_deleted_shapes",
    "mask_num_upsized_shapes",
    "num_pixel_corrections",
    "num_part_corrections",
    "delete_mask_polygon_count",
    "delete_mask_polygon_max",
    "delete_mask_polygon_min",
    "upsizing_mask_polygon_count",
    "upsizing_mask_polygon_max",
    "upsizing_mask_polygon_min",
    "number_of_optimized_partitions",
    "total_number_of_partitions",
    "parsing_time"
]


runtime_analysis_keys = [
    "target_prep_runtime",
    "ctm_fg",
    "qtm_fg",
    "ctm_prep",
    "qtm0_prep",
    "qtm1_prep",
    "qtm2_prep",
    "qtm3_prep",
    "qtm4_prep",
    "qtm5_prep",
    "qtm0_total",
    "qtm1_total",
    "qtm2_total",
    "qtm3_total",
    "qtm4_total",
    "qtm5_total",
    "ctm_exec_time",
    "qtm_exec_time",
    "total_prediction_time",
    "mrc1_time",
    "mrc2_time",
    "mbf_exec_time",
    "postprocess_exec_time",
    "total_fermi_runtime",
    "the_checker_runtime"
]


geometric_analysis_keys = [
    "mrc_area_count",
    "mrc_area_max_value",
    "mrc_area_min_value",
    "mrc_area_marker_x",
    "mrc_area_marker_y",
    "imrcfix_max_correction_max_value",
    "imrcfix_total_number_of_fixed_mrc_width_errors_count",
    "imrcfix_total_number_of_partially_fixed_mrc_width_errors_count",
    "imrcfix_the_worst_width_error_overall_max_value",
    "imrcfix_total_number_of_fixed_mrc_spacing_errors_count",
    "imrcfix_total_number_of_partially_fixed_mrc_spacing_errors_count",
    "imrcfix_the_worst_spacing_error_overall_max_value",
    "imrcfix_total_number_of_unimproved_mrc_errors_count",
    "high_curvature_internal_checking_setting",
    "high_curvature_external_checking_setting",
    "mrc_area_setting",
    "mrc_spacing_setting",
    "mrc_width_setting",
    "mrc_width_count",
    "mrc_width_max_value",
    "mrc_width_min_value",
    "mrc_width_marker_x",
    "mrc_width_marker_y",
    "mrc_spacing_count",
    "mrc_spacing_max_value",
    "mrc_spacing_min_value",
    "mrc_spacing_marker_x",
    "mrc_spacing_marker_y",
    "high_curvature_internal_checking_count",
    "high_curvature_internal_checking_max_value",
    "high_curvature_internal_checking_min_value",
    "high_curvature_internal_checking_marker_x",
    "high_curvature_internal_checking_marker_y",
    "high_curvature_external_checking_count",
    "high_curvature_external_checking_max_value",
    "high_curvature_external_checking_min_value",
    "high_curvature_external_checking_marker_x",
    "high_curvature_external_checking_marker_y",
    "xor_error_of_nominal_contour_greater_than_15_count",
    "xor_error_of_nominal_contour_greater_than_15_max_value",
    "xor_error_of_nominal_contour_greater_than_15_min_value",
    "xor_error_of_nominal_contour_greater_than_15_marker_x",
    "xor_error_of_nominal_contour_greater_than_15_marker_y",
    "xor_error_of_negative_dose_greater_than_15_count",
    "xor_error_of_negative_dose_greater_than_15_max_value",
    "xor_error_of_negative_dose_greater_than_15_min_value",
    "xor_error_of_negative_dose_greater_than_15_marker_x",
    "xor_error_of_negative_dose_greater_than_15_marker_y",
    "xor_error_of_positive_dose_greater_than_15_count",
    "xor_error_of_positive_dose_greater_than_15_max_value",
    "xor_error_of_positive_dose_greater_than_15_min_value",
    "xor_error_of_positive_dose_greater_than_15_marker_x",
    "xor_error_of_positive_dose_greater_than_15_marker_y",
    "xor_error_of_negative_defocus_greater_than_15_count",
    "xor_error_of_negative_defocus_greater_than_15_max_value",
    "xor_error_of_negative_defocus_greater_than_15_min_value",
    "xor_error_of_negative_defocus_greater_than_15_marker_x",
    "xor_error_of_negative_defocus_greater_than_15_marker_y",
    "xor_error_of_positive_defocus_greater_than_15_count",
    "xor_error_of_positive_defocus_greater_than_15_max_value",
    "xor_error_of_positive_defocus_greater_than_15_min_value",
    "xor_error_of_positive_defocus_greater_than_15_marker_x",
    "xor_error_of_positive_defocus_greater_than_15_marker_y"
]

statistical_analysis = [
    "mean_fermi",
    "std_fermi",
    "max_fermi",
    "count_fermi",
    "marker_x_fermi",
    "marker_y_fermi"
]

def extract_and_copy_values(file_path, keys):
    # Extract values
    extracted_values = {key: None for key in keys}
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            for key in keys:
                if line.startswith(key + " ="):
                    value = line.split("=", 1)[1].strip()
                    extracted_values[key] = value
                    break

    # Deep copy the extracted values
    copied_values = copy.deepcopy(extracted_values)
    
    return copied_values

def extract_statistical_sets(file_path, keys):
    statistical_data = []
    current_set = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            for key in keys:
                if line.startswith(key + " ="):
                    value = line.split("=", 1)[1].strip()
                    current_set[key] = value
                    break
            
            # If the current set is complete, store it and start a new one
            if len(current_set) == len(keys):
                statistical_data.append(current_set)
                current_set = {}

    # Store the last set if it wasn't added yet
    if current_set:
        statistical_data.append(current_set)

    return statistical_data

def write_to_fermi_file(output_path, main_stats, runtime_analysis_stats, geometric_analysis_stats, statistical_sets):
    with open(output_path, 'w') as file:
        file.write('[Main_Stats]\n')
        for key, value in main_stats.items():
            file.write(f"{key}: {value}\n")
        file.write('\n')

        file.write('[Runtime_Analysis_Stats]\n')
        for key, value in runtime_analysis_stats.items():
            file.write(f"{key}: {value}\n")
        file.write('\n')

        file.write('[Geometric_Analysis_Stats_Fermi]\n')
        for key, value in geometric_analysis_stats.items():
            file.write(f"{key}: {value}\n")
        file.write('\n')

        file.write('[Statistical_Analysis]\n')
        for i, stat_set in enumerate(statistical_sets):
            file.write(f"Set {i+1}:\n")
            for key, value in stat_set.items():
                file.write(f"  {key}: {value}\n")
            file.write('\n')

# Set up logging to create a log file for every stat we add to fermi.txt
def setup_logging(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'script.log')

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )

def log_and_extract_value(content, key):
    pattern = key + " ="
    for line in content:
        if line.startswith(pattern):
            value = line.split("=", 1)[1].strip()
            logging.info(f"{key} found ({value}).")
            return value
    logging.error(f"{key} not found.")
    return "None"

def extract_and_log_values(log_file_path, keys):
    with open(log_file_path, 'r') as file:
        content = file.readlines()

    extracted_values = {}
    for key in keys:
        extracted_values[key] = log_and_extract_value(content, key)

    return extracted_values

def main():
    parser = argparse.ArgumentParser(
        description="Parse log files and generate fermi.txt in the specified directory structure.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-l', '--location', required=True, help='Base location where the fermi.txt file will be placed (the folder containing the run directories).')
    parser.add_argument('-id', '--run_id', required=True, help='ID of the run (the name of the run directory, e.g., "11610").')
    parser.add_argument('-p', '--parse', action='store_true', help='Parse the log file and create fermi.txt.')
    parser.add_argument('-r', '--rsync', help='Optional rsync directory (outside the normal run folder) where fermi.txt should be placed.')

    args = parser.parse_args()

    # Determine the output directory where the fermi.txt will be placed
    if args.rsync:
        output_dir = os.path.join(args.rsync, args.run_id, 'qor')
        os.makedirs(output_dir, exist_ok=True)
    else:
        output_dir = os.path.join(args.location, args.run_id, 'qor')
        os.makedirs(output_dir, exist_ok=True)

    # Setup logging in the logs directory
    log_dir = os.path.join(output_dir, 'logs')
    setup_logging(log_dir)

    # Determine the output file path for fermi.txt
    output_file_path = os.path.join(output_dir, 'fermi.txt')
    if os.path.exists(output_file_path):
        print(f"fermi.txt has been created at {output_file_path}")
    else:
        print(f"Error: Failed to create fermi.txt at {output_file_path}")


    # Log file path assumed to be in the same directory where the script is executed
    log_file_path = os.path.join(os.getcwd(), 'dummy_logfile.txt')  
    if not os.path.exists(log_file_path):
        logging.error(f"Log file not found at {log_file_path}")
        print(f"Error: Log file not found at {log_file_path}")
        return
    
    # Extract data from the log file with logging
    main_stats = extract_and_log_values(log_file_path, main_keys)
    runtime_analysis_stats = extract_and_log_values(log_file_path, runtime_analysis_keys)
    geometric_analysis_stats = extract_and_log_values(log_file_path, geometric_analysis_keys)
    statistical_sets = extract_statistical_sets(log_file_path, statistical_analysis)  
    
    # Write the parsed data to fermi.txt
    write_to_fermi_file(output_file_path, main_stats, runtime_analysis_stats, geometric_analysis_stats, statistical_sets)

    print(f"fermi.txt has been created at {output_file_path}")
    print(f"Log file has been created at {os.path.join(log_dir, 'script.log')}")

if __name__ == '__main__':
    main()