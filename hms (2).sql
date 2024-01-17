-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 07, 2019 at 05:22 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kavya`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `Booking_ID` int(4) NOT NULL,
  `Booking_Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Room_No` int(4) NOT NULL,
  `Room_Type` varchar(20) NOT NULL,
  `Food_ID` int(4) NOT NULL,
  `Food_Type` varchar(20) NOT NULL,
  `Room_Charges` decimal(10,0) NOT NULL,
  `days` int(2) NOT NULL,
  `amount` decimal(10,0) NOT NULL,
  `Food_Charges` decimal(10,0) NOT NULL,
  `Grand_Total` decimal(10,0) NOT NULL,
  `UserName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`Booking_ID`, `Booking_Date`, `Room_No`, `Room_Type`, `Food_ID`, `Food_Type`, `Room_Charges`, `days`, `amount`, `Food_Charges`, `Grand_Total`, `UserName`) VALUES
(1, '2019-08-28 10:51:50', 105, 'SUPER-DELUXE', 1, 'Veg', '7000', 2, '14000', '1200', '15200', 'kavya'),
(2, '2019-08-28 10:53:38', 102, 'AC', 3, 'Vegan', '4000', 5, '20000', '1800', '21800', 'tanu'),
(5, '2019-09-07 03:10:46', 103, 'DELUXE', 4, 'Beverages', '5000', 1, '5000', '2000', '7000', 'naman');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(4) NOT NULL,
  `name` varchar(30) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `username`, `password`, `mobile`, `email`, `address`) VALUES
(1, 'Kavya', 'kavya', '12345', '9876543210', 'kb@gmail.com', 'Vashi'),
(8, 'Tanu', 'tanu', '12345', '1234567890', 'tanu@gmail.com', 'New Panvel'),
(9, 'Naman', 'naman', '12345', '9182736450', 'nb@gmail.com', 'Vashi');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `emp_id` int(4) NOT NULL,
  `Emp_name` varchar(30) NOT NULL,
  `desig` varchar(30) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_id`, `Emp_name`, `desig`, `username`, `password`, `mobile`, `email`, `address`) VALUES
(111, 'Kavya Bansal', 'Manager', 'admin', '12345', '7208808034', 'kavya@gmail.com', 'New Panvel'),
(112, 'Tanu', 'Room Service', 'tanu', '12345', '9594927299', 'tanu@gmail.com', 'Panvel');

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

CREATE TABLE `food` (
  `food_id` int(3) NOT NULL,
  `Food_Type` varchar(40) NOT NULL,
  `Charges` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`food_id`, `Food_Type`, `Charges`) VALUES
(1, 'chinese', '1200'),
(2, 'continental', '1500'),
(3, 'french', '1800'),
(4, 'italian', '1800'),
(5, 'indian', '1550'),
(6, 'mexican', '1500'),
(7, 'fusion', '3000');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `Room_No` int(3) NOT NULL,
  `Room_Type` varchar(20) NOT NULL,
  `Charges` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`Room_No`, `Room_Type`, `Charges`) VALUES
(101, 'AC', '4000'),
(102, 'AC', '4000'),
(103, 'DELUXE', '5000'),
(104, 'DELUXE', '5000'),
(105, 'SUPER-DELUXE', '7000'),
(106, 'SUPER-DELUXE', '7000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`Booking_ID`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `food`
--
ALTER TABLE `food`
  ADD PRIMARY KEY (`food_id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`Room_No`);


--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `Booking_ID` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `food`
--
ALTER TABLE `food`
  MODIFY `food_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `Room_No` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
