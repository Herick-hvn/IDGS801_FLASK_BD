-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 13, 2023 at 08:34 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `idgs801`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_teacher` (IN `id_` INT(50))  NO SQL
DELETE FROM teachers WHERE id = id_$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_teacher` (IN `name` VARCHAR(50), IN `surname` VARCHAR(50), IN `email` VARCHAR(50), IN `created_date` DATE)  NO SQL
INSERT into teachers VALUES (id, name, surname, email, created_date)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `search_all_teachers` ()  NO SQL
SELECT * from teachers$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `search_teacher` (IN `id_` INT(30))  NO SQL
SELECT * FROM teachers WHERE id = id_$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_teacher` (IN `id_` INT(50), IN `name` VARCHAR(50), IN `surname` VARCHAR(50), IN `email` VARCHAR(50))  NO SQL
UPDATE teachers
SET name = name,
    surname = surname,
    email = email,
    created_date = created_date
WHERE id = id_$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `alumnos`
--

CREATE TABLE `alumnos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `email` varchar(120) NOT NULL,
  `create_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `alumnos`
--

INSERT INTO `alumnos` (`id`, `nombre`, `apellidos`, `email`, `create_date`) VALUES
(1, 'herick', 'vazquez ', 'navarro@gmai.com', '2023-03-09 14:37:21');

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE `teachers` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `created_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`id`, `name`, `surname`, `email`, `created_date`) VALUES
(4, 'Sophia', 'Brown', 'sophia.brown@example.com', '2022-01-04'),
(5, 'William', 'Jones', 'william.jones@example.com', '2022-01-05'),
(6, 'Ava', 'Garcia', 'ava.garcia@example.com', '2022-01-06'),
(7, 'David', 'Miller', 'david.miller@example.com', '2022-01-07'),
(8, 'Olivia', 'Davis', 'olivia.davis@example.com', '2022-01-08'),
(9, 'Daniel', 'Martinez', 'daniel.martinez@example.com', '2022-01-09'),
(10, 'Isabella', 'Lopez', 'isabella.lopez@example.com', '2022-01-10'),
(11, 'Prueba', 'prueba', 'fs@df', '2023-03-13'),
(12, 'Herick', 'Vazquez', 'gtherick1390@gmail.com', '2023-03-13'),
(13, 'prueba', 'vazquez', 'clouf@gmal.com', '2023-03-13'),
(14, 'Herick', 'Heman', 'cloudvn1390@gmail.com', '2023-03-13');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
