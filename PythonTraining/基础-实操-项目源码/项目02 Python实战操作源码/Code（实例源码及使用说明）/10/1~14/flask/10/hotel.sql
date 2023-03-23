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
