-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.36 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.7.0.6850
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for db_cuaca
CREATE DATABASE IF NOT EXISTS `db_cuaca` /*!40100 DEFAULT CHARACTER SET armscii8 COLLATE armscii8_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_cuaca`;

-- Dumping structure for table db_cuaca.tb_cuaca
CREATE TABLE IF NOT EXISTS `tb_cuaca` (
  `id` int NOT NULL,
  `suhu` int DEFAULT NULL,
  `humid` int DEFAULT NULL,
  `lux` int DEFAULT NULL,
  `ts` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Dumping data for table db_cuaca.tb_cuaca: ~20 rows (approximately)
REPLACE INTO `tb_cuaca` (`id`, `suhu`, `humid`, `lux`, `ts`) VALUES
	(1, 31, 29, 25, '2024-09-13 11:02:10'),
	(2, 25, 35, 26, '2024-11-07 16:03:05'),
	(3, 22, 25, 36, '2024-11-08 10:03:40'),
	(4, 29, 29, 21, '2024-11-22 06:06:10'),
	(5, 36, 32, 29, '2024-01-13 16:25:44'),
	(6, 33, 23, 35, '2024-06-23 17:07:28'),
	(7, 25, 34, 31, '2024-02-03 19:09:07'),
	(8, 24, 35, 22, '2023-11-13 16:09:40'),
	(9, 29, 22, 30, '2024-10-17 10:10:53'),
	(10, 30, 27, 29, '2024-11-13 03:11:27'),
	(11, 22, 30, 24, '2024-12-22 07:11:47'),
	(12, 31, 28, 33, '2023-11-04 15:12:32'),
	(13, 31, 35, 21, '2024-09-09 12:13:05'),
	(14, 23, 23, 27, '2024-04-13 17:13:29'),
	(15, 22, 30, 24, '2024-11-03 06:14:25'),
	(16, 33, 29, 22, '2024-07-29 13:14:58'),
	(17, 29, 33, 26, '2021-11-13 16:15:36'),
	(18, 31, 32, 31, '2023-08-13 13:16:00'),
	(19, 30, 24, 36, '2024-11-11 21:16:31'),
	(20, 36, 30, 32, '2024-10-10 12:17:19');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
