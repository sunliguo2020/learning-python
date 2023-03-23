/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : flask_demo

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2019-06-25 10:19:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------

-- ----------------------------
-- Table structure for classes
-- ----------------------------
DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of classes
-- ----------------------------
INSERT INTO `classes` VALUES ('2', 'Chinese');
INSERT INTO `classes` VALUES ('1', 'English');

-- ----------------------------
-- Table structure for hotel
-- ----------------------------
DROP TABLE IF EXISTS `hotel`;
CREATE TABLE `hotel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `brand` varchar(64) DEFAULT NULL,
  `features` varchar(64) DEFAULT NULL,
  `score` float DEFAULT NULL,
  `price` float DEFAULT NULL,
  `decorate_time` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of hotel
-- ----------------------------
INSERT INTO `hotel` VALUES ('1', '时光漫步怀旧主题酒店(北京国家体育总局天坛店)', '4', '漫步时光', '舒适型', '4.7', '463', '2017-04-23');
INSERT INTO `hotel` VALUES ('2', '北京五环大酒店', '5', '五环', '舒适型', '4', '334', '2012-04-23');
INSERT INTO `hotel` VALUES ('3', '北京望京798和颐酒店', '3', '和颐', '居家型', '4.4', '562', '2011-04-23');
INSERT INTO `hotel` VALUES ('4', '和颐酒店(北京三里屯店)', '5', '和颐', '高档型', '4.6', '536', '2011-04-23');

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('1', 'Andy', '694798056@qq.com');
INSERT INTO `students` VALUES ('2', 'Jack', 'jack@qq.com');
INSERT INTO `students` VALUES ('3', 'Kobe', 'kobe@qq.com');

-- ----------------------------
-- Table structure for student_identifier
-- ----------------------------
DROP TABLE IF EXISTS `student_identifier`;
CREATE TABLE `student_identifier` (
  `class_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  KEY `class_id` (`class_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `student_identifier_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`),
  CONSTRAINT `student_identifier_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `students` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student_identifier
-- ----------------------------
INSERT INTO `student_identifier` VALUES ('1', '1');
INSERT INTO `student_identifier` VALUES ('1', '2');
INSERT INTO `student_identifier` VALUES ('2', '1');
INSERT INTO `student_identifier` VALUES ('2', '3');
