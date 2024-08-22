-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: emumbaqor
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `geometric_analysis`
--

DROP TABLE IF EXISTS `geometric_analysis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `geometric_analysis` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `property` varchar(100) NOT NULL,
  `value` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `job_id` (`job_id`),
  CONSTRAINT `geometric_analysis_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `geometric_analysis`
--

LOCK TABLES `geometric_analysis` WRITE;
/*!40000 ALTER TABLE `geometric_analysis` DISABLE KEYS */;
INSERT INTO `geometric_analysis` VALUES (1,1,'mrc_area_count','0'),(2,1,'mrc_area_max_value','0.0'),(3,1,'mrc_area_min_value','0.0'),(4,1,'mrc_area_marker_x','0'),(5,1,'mrc_area_marker_y','0'),(6,1,'imrcfix_max_correction_max_value',NULL),(7,1,'imrcfix_total_number_of_fixed_mrc_width_errors_count',NULL),(8,1,'imrcfix_total_number_of_partially_fixed_mrc_width_errors_count',NULL),(9,1,'imrcfix_the_worst_width_error_overall_max_value',NULL),(10,1,'imrcfix_total_number_of_fixed_mrc_spacing_errors_count',NULL),(11,1,'imrcfix_total_number_of_partially_fixed_mrc_spacing_errors_count',NULL),(12,1,'imrcfix_the_worst_spacing_error_overall_max_value',NULL),(13,1,'imrcfix_total_number_of_unimproved_mrc_errors_count',NULL),(14,1,'high_curvature_internal_checking_setting','7'),(15,1,'high_curvature_external_checking_setting','7'),(16,1,'mrc_area_setting','520'),(17,1,'mrc_spacing_setting','13.0'),(18,1,'mrc_width_setting','13.0'),(19,1,'mrc_width_count','0'),(20,1,'mrc_width_max_value','0.0'),(21,1,'mrc_width_min_value','0.0'),(22,1,'mrc_width_marker_x','0'),(23,1,'mrc_width_marker_y','0'),(24,1,'mrc_spacing_count','0'),(25,1,'mrc_spacing_max_value','0.0'),(26,1,'mrc_spacing_min_value','0.0'),(27,1,'mrc_spacing_marker_x','0'),(28,1,'mrc_spacing_marker_y','0'),(29,1,'high_curvature_internal_checking_count','0'),(30,1,'high_curvature_internal_checking_max_value','0.0'),(31,1,'high_curvature_internal_checking_min_value','0.0'),(32,1,'high_curvature_internal_checking_marker_x','0'),(33,1,'high_curvature_internal_checking_marker_y','0'),(34,1,'high_curvature_external_checking_count','0'),(35,1,'high_curvature_external_checking_max_value','0.0'),(36,1,'high_curvature_external_checking_min_value','0.0'),(37,1,'high_curvature_external_checking_marker_x','0'),(38,1,'high_curvature_external_checking_marker_y','0'),(39,1,'xor_error_of_nominal_contour_greater_than_15_count','0'),(40,1,'xor_error_of_nominal_contour_greater_than_15_max_value','0.0'),(41,1,'xor_error_of_nominal_contour_greater_than_15_min_value','0.0'),(42,1,'xor_error_of_nominal_contour_greater_than_15_marker_x','0'),(43,1,'xor_error_of_nominal_contour_greater_than_15_marker_y','0'),(44,1,'xor_error_of_negative_dose_greater_than_15_count','0'),(45,1,'xor_error_of_negative_dose_greater_than_15_max_value','0.0'),(46,1,'xor_error_of_negative_dose_greater_than_15_min_value','0.0'),(47,1,'xor_error_of_negative_dose_greater_than_15_marker_x','0'),(48,1,'xor_error_of_negative_dose_greater_than_15_marker_y','0'),(49,1,'xor_error_of_positive_dose_greater_than_15_count','0'),(50,1,'xor_error_of_positive_dose_greater_than_15_max_value','0.0'),(51,1,'xor_error_of_positive_dose_greater_than_15_min_value','0.0'),(52,1,'xor_error_of_positive_dose_greater_than_15_marker_x','0'),(53,1,'xor_error_of_positive_dose_greater_than_15_marker_y','0'),(54,1,'xor_error_of_negative_defocus_greater_than_15_count','0'),(55,1,'xor_error_of_negative_defocus_greater_than_15_max_value','0.0'),(56,1,'xor_error_of_negative_defocus_greater_than_15_min_value','0.0'),(57,1,'xor_error_of_negative_defocus_greater_than_15_marker_x','0'),(58,1,'xor_error_of_negative_defocus_greater_than_15_marker_y','0'),(59,1,'xor_error_of_positive_defocus_greater_than_15_count','0'),(60,1,'xor_error_of_positive_defocus_greater_than_15_max_value','0.0'),(61,1,'xor_error_of_positive_defocus_greater_than_15_min_value','0.0'),(62,1,'xor_error_of_positive_defocus_greater_than_15_marker_x','0'),(63,1,'xor_error_of_positive_defocus_greater_than_15_marker_y','0');
/*!40000 ALTER TABLE `geometric_analysis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_name` varchar(100) DEFAULT NULL,
  `fermi_job_id` varchar(50) DEFAULT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_user_id` (`user_id`),
  KEY `idx_fermi_job_id` (`fermi_job_id`),
  KEY `idx_job_name` (`job_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` VALUES (1,'exampleDesign01',NULL,'exampleuser','2024-08-20 17:56:18');
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_stats`
--

DROP TABLE IF EXISTS `main_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_stats` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `property` varchar(100) NOT NULL,
  `value` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `job_id` (`job_id`),
  CONSTRAINT `main_stats_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_stats`
--

LOCK TABLES `main_stats` WRITE;
/*!40000 ALTER TABLE `main_stats` DISABLE KEYS */;
INSERT INTO `main_stats` VALUES (1,1,'fermi_id',NULL),(2,1,'checker_id',NULL),(3,1,'gpu','4'),(4,1,'expect_run_time_50_gpu','720.15'),(5,1,'expect_run_time_1_gpu','34500.25'),(6,1,'user','exampleuser'),(7,1,'name','exampleDesign01'),(8,1,'max_err_per_partion',NULL),(9,1,'total_errors',NULL),(10,1,'design_size','0.85785 x 0.844296'),(11,1,'mask_file_size','2258.88'),(12,1,'recipe_name',NULL),(13,1,'mbf_size','2662.4'),(14,1,'pdose_simulation_size','413.95'),(15,1,'pdefocus_simulation_size','430.4'),(16,1,'ndefocus_simulation_size','430.4'),(17,1,'nominal_simulation_size','435.32'),(18,1,'ndose_simulation_size','459.48'),(19,1,'target_file_size','355.67'),(20,1,'machine_name','cdp51'),(21,1,'run_date_time','2024-08-01 14:47:29.786043'),(22,1,'revision_branch',NULL),(23,1,'revision_commit',NULL),(24,1,'revision_date',NULL),(25,1,'fermi_job_name',NULL),(26,1,'tmod_name',NULL),(27,1,'process_condition',NULL),(28,1,'partition','36 x 36'),(29,1,'grid','8'),(30,1,'optimizer_iterations',NULL),(31,1,'force_flag','False'),(32,1,'force_screenshot','False'),(33,1,'mpi_retry_count',NULL),(34,1,'num_qtm3_iterations',NULL),(35,1,'num_qtm4_iterations',NULL),(36,1,'num_qtm5_iterations',NULL),(37,1,'mask_num_deleted_shapes',NULL),(38,1,'mask_num_upsized_shapes',NULL),(39,1,'num_pixel_corrections',NULL),(40,1,'num_part_corrections',NULL),(41,1,'delete_mask_polygon_count',NULL),(42,1,'delete_mask_polygon_max',NULL),(43,1,'delete_mask_polygon_min',NULL),(44,1,'upsizing_mask_polygon_count',NULL),(45,1,'upsizing_mask_polygon_max',NULL),(46,1,'upsizing_mask_polygon_min',NULL),(47,1,'number_of_optimized_partitions','1024'),(48,1,'total_number_of_partitions','1024'),(49,1,'parsing_time','False');
/*!40000 ALTER TABLE `main_stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `runtime_analysis`
--

DROP TABLE IF EXISTS `runtime_analysis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `runtime_analysis` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `property` varchar(100) NOT NULL,
  `value` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `job_id` (`job_id`),
  CONSTRAINT `runtime_analysis_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `runtime_analysis`
--

LOCK TABLES `runtime_analysis` WRITE;
/*!40000 ALTER TABLE `runtime_analysis` DISABLE KEYS */;
INSERT INTO `runtime_analysis` VALUES (1,1,'target_prep_runtime','420.75'),(2,1,'ctm_fg','830.40'),(3,1,'qtm_fg','3960.60'),(4,1,'ctm_prep','2300.25'),(5,1,'qtm0_prep','880.00'),(6,1,'qtm1_prep','1070.50'),(7,1,'qtm2_prep','1150.60'),(8,1,'qtm3_prep','630.75'),(9,1,'qtm4_prep','0'),(10,1,'qtm5_prep','0'),(11,1,'qtm0_total','1300.00'),(12,1,'qtm1_total','1650.75'),(13,1,'qtm2_total','2000.90'),(14,1,'qtm3_total','4550.00'),(15,1,'qtm4_total','0'),(16,1,'qtm5_total','0'),(17,1,'ctm_exec_time','3200.00'),(18,1,'qtm_exec_time','11200.00'),(19,1,'total_prediction_time',NULL),(20,1,'mrc1_time','1350.25'),(21,1,'mrc2_time','500.00'),(22,1,'mbf_exec_time','200.00'),(23,1,'postprocess_exec_time','1400.00'),(24,1,'total_fermi_runtime','16200.00'),(25,1,'the_checker_runtime',NULL);
/*!40000 ALTER TABLE `runtime_analysis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statistical_analysis`
--

DROP TABLE IF EXISTS `statistical_analysis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statistical_analysis` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `set_id` int NOT NULL,
  `property` varchar(100) NOT NULL,
  `value` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `job_id` (`job_id`),
  CONSTRAINT `statistical_analysis_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statistical_analysis`
--

LOCK TABLES `statistical_analysis` WRITE;
/*!40000 ALTER TABLE `statistical_analysis` DISABLE KEYS */;
INSERT INTO `statistical_analysis` VALUES (1,1,1,'mean_fermi','5.75'),(2,1,1,'std_fermi','0.81'),(3,1,1,'max_fermi','10.01'),(4,1,1,'count_fermi','820367'),(5,1,1,'marker_x_fermi','635002.5'),(6,1,1,'marker_y_fermi','165332.7'),(7,1,2,'mean_fermi','-0.58'),(8,1,2,'std_fermi','0.49'),(9,1,2,'max_fermi','4.15'),(10,1,2,'count_fermi','345000'),(11,1,2,'marker_x_fermi','840000.0'),(12,1,2,'marker_y_fermi','33500.0'),(13,1,3,'mean_fermi','3.10'),(14,1,3,'std_fermi','0.62'),(15,1,3,'max_fermi','6.60'),(16,1,3,'count_fermi','850000'),(17,1,3,'marker_x_fermi','690000.0'),(18,1,3,'marker_y_fermi','134000.0'),(19,1,4,'mean_fermi','-2.65'),(20,1,4,'std_fermi','0.64'),(21,1,4,'max_fermi','5.80'),(22,1,4,'count_fermi','800000'),(23,1,4,'marker_x_fermi','840000.0'),(24,1,4,'marker_y_fermi','34000.0'),(25,1,5,'mean_fermi','-0.06'),(26,1,5,'std_fermi','0.42'),(27,1,5,'max_fermi','2.85'),(28,1,5,'count_fermi','8900'),(29,1,5,'marker_x_fermi','835000.0'),(30,1,5,'marker_y_fermi','33500.0'),(31,1,6,'mean_fermi','-1.15'),(32,1,6,'std_fermi','0.51'),(33,1,6,'max_fermi','3.80'),(34,1,6,'count_fermi','30000'),(35,1,6,'marker_x_fermi','828000.0'),(36,1,6,'marker_y_fermi','36000.0');
/*!40000 ALTER TABLE `statistical_analysis` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-21 11:26:47
