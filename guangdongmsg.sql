/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50022
Source Host           : localhost:3306
Source Database       : guangdongmsg

Target Server Type    : MYSQL
Target Server Version : 50022
File Encoding         : 65001

Date: 2017-04-28 21:03:53
*/
DROP DATABASE IF EXISTS t_guangdong;
CREATE DATABASE `t_guangdong` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `t_guangdong`;
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for guangdongmsg
-- ----------------------------
DROP TABLE IF EXISTS `guangdongmsg`;
CREATE TABLE `guangdongmsg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_no` varchar(200) DEFAULT NULL,
  `case_name` varchar(200) DEFAULT NULL,
  `punish_type1` varchar(200) DEFAULT NULL,
  `punish_type2` varchar(200) DEFAULT NULL,
  `punish_reason` varchar(500) DEFAULT NULL,
  `law_item` varchar(800) DEFAULT NULL,
  `punish_result` varchar(800) DEFAULT NULL,
  `entity_name` varchar(200) DEFAULT NULL,
  `credit_no` varchar(200) DEFAULT NULL,
  `org_code` varchar(200) DEFAULT NULL,
  `reg_no` varchar(200) DEFAULT NULL,
  `tax_no` varchar(200) DEFAULT NULL,
  `identity_card` varchar(200) DEFAULT NULL,
  `legal_man` varchar(200) DEFAULT NULL,
  `punish_date` varchar(200) DEFAULT NULL,
  `punish_agent` varchar(200) DEFAULT NULL,
  `area_code` varchar(200) DEFAULT NULL,
  `current_status` varchar(200) DEFAULT NULL,
  `offical_updtime` varchar(200) DEFAULT NULL,
  `note` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
