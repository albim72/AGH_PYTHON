-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: logindatabase
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_user`
--

DROP TABLE IF EXISTS `tbl_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  `user_username` varchar(45) NOT NULL,
  `user_password` varchar(500) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_username_UNIQUE` (`user_username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user`
--

LOCK TABLES `tbl_user` WRITE;
/*!40000 ALTER TABLE `tbl_user` DISABLE KEYS */;
INSERT INTO `tbl_user` VALUES (1,'Jan','janek','ffffff4444'),(2,'tytry','rtyrty','pbkdf2:sha256:260000$r8ejulL3Ki1SFbmU$252f89472a440af0e1b26d37bd82e8d6bf8c5c1f1144a77acd5b12eb4449ad59'),(3,'rttrurtu','5rrtyutrurtu','pbkdf2:sha256:260000$AyZpjRkNTBU7sJ9Y$301391180857ef8306ad7d975efa6318b87533aaf43c578c9bed80995d07c8d8'),(4,'5678','678678','pbkdf2:sha256:260000$UbwTAiCbDk0lttMK$723bec94e62691fc001e3fe505505e0525d7890629af5c153b8904be9fbedb13'),(5,'uy','ttyutyu','pbkdf2:sha256:260000$cDK806Fk2zoj6RnR$17ff25c2adc7c9ef7f6ba31e43b03cd422c148ba790fd33d4d279ce44ec30e69'),(6,'wefewfwe','fwefwefew','pbkdf2:sha256:260000$gQOkjmJPH9UvrBDA$9fd1d7edd3ecb0f1181e35c904738ce434acc2187c938a2257bfe36472ec950c'),(7,'Marcin','marc@wp.pl','pbkdf2:sha256:260000$AgWzP8ICap4wQGpx$1c6fedab311e40a072db0e82775c0cd3769f2a420e15707846c0471310d56c03'),(8,'Marcin','marcin@wp.pl','pbkdf2:sha256:260000$RnuCFzbXq6rfLTym$a4ea3acd2a54c821cd88002472baf980047368f64c0b824011087a7755573e0f'),(9,'Marcin','sss@w.pl','pbkdf2:sha256:260000$7shylh3Uuwzflknm$af7d5224c755e155b2c338ac6a4cddaa55f8056ddcd5ad33ee6ee1473abaee21'),(10,'Ania','ania@ddd.pl','pbkdf2:sha256:260000$JJMoNsb9TsAKBl1b$76425d7807debf7b75a5e31578976ff317c6d9166d54f487b3f04a9eb65b71b7');
/*!40000 ALTER TABLE `tbl_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-13 19:53:51
