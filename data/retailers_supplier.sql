-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: retailers
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `sup_id` int NOT NULL,
  'mob_no' bigint CHECK (LENGTH(mob_no) = 10),
  `prod_id` int NOT NULL,

  `product_name` varchar(255) NOT NULL,
  `purchase_price` decimal(10,2) NOT NULL,
  `quantity_bought` int NOT NULL,
  `sales_price_perunit` decimal(10,2) NOT NULL,
  `gst` varchar(10) DEFAULT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `low_stockalert` int DEFAULT NULL,
  `purchase_month` int DEFAULT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,2,4,'WaterBottles 500ml',450.00,10,500.00,'12',5310.00,5,4),(2,2,2,'Eggs',4.00,20,6.00,'5',80.00,4,2),(3,2,3,'A4 Sheets 200 pages',345.00,23,3242.00,'5',7935.00,2,5),(4,2,2,'Eggs',32.00,42,324.00,'6',1344.00,2,1),(5,1,6,'Headphones black',4000.00,4,6599.00,'28',20480.00,1,3),(6,2,2,'Eggs',3.00,3,7.00,'5',9.45,2,4),(7,2,4,'WaterBottles 500ml',450.00,4,550.00,'12',2016.00,5,4),(8,2,2,'Eggs',3.00,3,7.00,'5',9.45,2,4),(9,4,7,'Classmate Notebook ',55.00,24,75.00,'12',1478.40,4,4);
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-21 16:06:50
