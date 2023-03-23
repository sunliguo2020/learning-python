/*
Navicat MySQL Data Transfer

Source Server         : studyPython
Source Server Version : 50722
Source Host           : localhost:3306
Source Database       : jd_data

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-04-19 11:19:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for heat_rankings
-- ----------------------------
DROP TABLE IF EXISTS `heat_rankings`;
CREATE TABLE `heat_rankings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(45) DEFAULT NULL,
  `jd_price` varchar(10) DEFAULT NULL,
  `ding_price` varchar(10) DEFAULT NULL,
  `press` varchar(45) DEFAULT NULL,
  `item_url` varchar(45) DEFAULT NULL,
  `jd_id` varchar(45) DEFAULT NULL,
  `middle_time` varchar(45) DEFAULT NULL,
  `poor_time` varchar(45) DEFAULT NULL,
  `attention_price` varchar(45) DEFAULT NULL,
  `attention` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of heat_rankings
-- ----------------------------
INSERT INTO `heat_rankings` VALUES ('1', '深入理解Java虚拟机：JVM高级特性与最佳实践（第2版）', '65.20', '79.00', '机械工业出版社', 'http://item.jd.com/11252778.html', '11252778', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('2', '架构即未来：现代企业可扩展的Web架构、流程和组织（原书第2版）', '81.70', '99.00', '机械工业出版社', 'http://item.jd.com/11905648.html', '11905648', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('3', '鸟哥的Linux私房菜 （基础学习篇 第三版） ', '71.90', '88.00', '人民邮电出版社', 'http://item.jd.com/10064429.html', '10064429', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('4', '鸟哥的Linux私房菜：服务器架设篇（第三版） ', '89.10', '108.00', '机械工业出版社', 'http://item.jd.com/11018248.html', '11018248', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('5', '数学之美（第二版）', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/11572052.html', '11572052', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('6', 'C Primer Plus 第6版 中文版 ', '72.70', '89.00', '人民邮电出版社', 'http://item.jd.com/11917487.html', '11917487', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('7', 'C Primer Plus（第5版 中文版）', '50.30', '60.00', '人民邮电出版社', 'http://item.jd.com/10062260.html', '10062260', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('8', '锋利的jQuery（第2版）', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/11019625.html', '11019625', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('9', 'JavaScript DOM编程艺术（第2版） ', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/10603153.html', '10603153', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('10', 'Java从入门到精通（第4版 附光盘）', '57.70', '69.60', '清华大学出版社', 'http://item.jd.com/11985075.html', '11985075', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('11', '机器学习【首届京东文学奖-年度新锐入围作品】', '75.10', '88.00', '清华大学出版社', 'http://item.jd.com/11867803.html', '11867803', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('12', '人工智能：一种现代的方法（第3版 影印版）', '138.30', '158.00', '清华大学出版社', 'http://item.jd.com/10779582.html', '10779582', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('13', '视觉机器学习20讲', '41.70', '49.00', '清华大学出版社', 'http://item.jd.com/11706776.html', '11706776', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('14', 'Word Excel PPT 2010办公应用从入门到精通（附DVD光盘1张）', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/11266264.html', '11266264', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('15', 'Python基础教程（第2版 修订版） ', '64.50', '79.00', '人民邮电出版社', 'http://item.jd.com/11461683.html', '11461683', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('16', 'Python核心编程（第3版） ', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11936238.html', '11936238', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('17', 'Python核心编程（第2版）', '74.50', '89.00', '人民邮电出版社', 'http://item.jd.com/10062788.html', '10062788', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('18', 'Photoshop CS6完全自学教程（中文版 附DVD光盘）', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11020038.html', '11020038', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('19', '大型网站技术架构 核心原理与案例分析', '48.20', '59.00', '电子工业出版社', 'http://item.jd.com/11322972.html', '11322972', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('20', 'Java虚拟机精讲', '55.00', '69.00', '电子工业出版社', 'http://item.jd.com/11631886.html', '11631886', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('21', 'Java核心技术系列：Java多线程编程核心技术', '56.90', '69.00', '机械工业出版社', 'http://item.jd.com/11701869.html', '11701869', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('22', 'Java并发编程的艺术 ', '48.70', '59.00', '机械工业出版社', 'http://item.jd.com/11740734.html', '11740734', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('23', 'Presto技术内幕', '37.00', '69.00', '电子工业出版社', 'http://item.jd.com/11906548.html', '11906548', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('24', 'Excel效率手册：早做完，不加班（套装共3册）', '64.80', '94.00', '清华大学出版社', 'http://item.jd.com/11680843.html', '11680843', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('25', '代码整洁之道 程序员的职业素养', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/11977659.html', '11977659', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('26', 'TCP/IP详解卷2：实现', '64.40', '78.00', '机械工业出版社', 'http://item.jd.com/10057318.html', '10057318', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('27', '启示录：打造用户喜爱的产品', '30.60', '36.00', '华中科技大学出版社', 'http://item.jd.com/10628082.html', '10628082', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('28', '谁说菜鸟不会数据分析（入门篇）（纪念版）（全彩）', '48.20', '59.00', '电子工业出版社', 'http://item.jd.com/11944656.html', '11944656', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('29', 'C++ Primer（中文版 第5版）', '104.60', '128.00', '电子工业出版社', 'http://item.jd.com/11306138.html', '11306138', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('30', '第一行代码 Android 第2版 ', '64.50', '79.00', '人民邮电出版社', 'http://item.jd.com/12012505.html', '12012505', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('31', 'Excel 2013公式与函数辞典646秘技大全（646秘技大全 全新升级版 附 ...', '35.90', '59.90', '中国青年出版社', 'http://item.jd.com/11356071.html', '11356071', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('32', 'PPT炼成记：高效能PPT达人的10堂必修课', '38.70', '49.90', '中国青年出版社', 'http://item.jd.com/11429319.html', '11429319', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('33', 'Excel2013数据透视表实战技巧精粹辞典（339秘技大全 超值双色版 附光盘 ...', '49.40', '59.90', '中国青年出版社', 'http://item.jd.com/11670751.html', '11670751', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('34', 'Office 2013实战技巧精粹辞典（超值双色版 附光盘）', '31.00', '59.00', '中国青年出版社', 'http://item.jd.com/11351487.html', '11351487', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('35', '疯狂Swift讲义（第2版）', '55.00', '69.00', '电子工业出版社', 'http://item.jd.com/11883734.html', '11883734', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('36', 'Cocos2d-x 3.X游戏开发实战（附光盘）', '70.20', '88.00', '电子工业出版社', 'http://item.jd.com/11596624.html', '11596624', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('37', '中文版Photoshop CS5完全自学教程（附光盘）', '82.90', '99.00', '人民邮电出版社', 'http://item.jd.com/10064569.html', '10064569', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('38', '说服力：工作型PPT该这样做（第2版）', '35.90', '49.00', '人民邮电出版社', 'http://item.jd.com/11452031.html', '11452031', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('39', 'JavaScript权威指南（第6版）', '114.70', '139.00', '机械工业出版社', 'http://item.jd.com/10974436.html', '10974436', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('40', '别怕，Excel VBA其实很简单（全新基础学习版）', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/11094550.html', '11094550', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('41', '计算机科学丛书：C程序设计语言（第2版・新版） ', '24.80', '30.00', '机械工业出版社', 'http://item.jd.com/10057446.html', '10057446', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('42', '图解密码技术 第3版', '72.70', '89.00', '人民邮电出版社', 'http://item.jd.com/11942019.html', '11942019', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('43', 'O\'Reilly：Head First设计模式（中文版）', '67.60', '98.00', '中国电力出版社', 'http://item.jd.com/10100236.html', '10100236', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('44', 'C++ Primer Plus（第6版 中文版） ', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11017238.html', '11017238', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('45', 'Excel 2013应用大全', '82.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11731534.html', '11731534', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('46', 'iOS开发指南 从Hello World到App Store上架 第4版', '94.90', '119.00', '人民邮电出版社', 'http://item.jd.com/11976900.html', '11976900', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('47', 'Objective-C基础教程 第2版', '49.40', '59.00', '人民邮电出版社', 'http://item.jd.com/11232703.html', '11232703', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('48', '精通iOS开发（第7版）', '94.10', '118.00', '人民邮电出版社', 'http://item.jd.com/11779940.html', '11779940', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('49', 'Swift基础教程', '39.10', '49.00', '人民邮电出版社', 'http://item.jd.com/11711347.html', '11711347', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('50', 'PHP和MySQL Web开发（原书第4版）', '73.80', '95.00', '机械工业出版社', 'http://item.jd.com/10059047.html', '10059047', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('51', 'HTML5+CSS3从入门到精通（附光盘）', '59.30', '69.80', '清华大学出版社', 'http://item.jd.com/11241686.html', '11241686', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('52', 'Effective Java中文版（第2版） ', '42.90', '52.00', '机械工业出版社', 'http://item.jd.com/10058902.html', '10058902', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('53', 'Axure RP8 实战手册 网站和APP原型制作案例精粹', '64.50', '79.00', '人民邮电出版社', 'http://item.jd.com/12034368.html', '12034368', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('54', 'Axure RP 7.0从入门到精通 Web + APP产品经理原型设计', '74.50', '89.00', '人民邮电出版社', 'http://item.jd.com/11853919.html', '11853919', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('55', 'Axure RP8 网站和APP原型制作 从入门到精通', '74.50', '89.00', '人民邮电出版社', 'http://item.jd.com/11898679.html', '11898679', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('56', 'Axure RP7 网站和APP原型制作从入门到精通 60小时案例版', '90.50', '108.00', '人民邮电出版社', 'http://item.jd.com/11931339.html', '11931339', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('57', '数据结构与算法分析：C语言描述（原书第2版） ', '28.90', '35.00', '机械工业出版社', 'http://item.jd.com/10057441.html', '10057441', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('58', 'HTML CSS JavaScript 网页制作从入门到精通 第3版', '41.00', '49.00', '人民邮电出版社', 'http://item.jd.com/11993156.html', '11993156', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('59', 'Excel 2013数据透视表应用大全', '72.20', '99.00', '北京大学出版社', 'http://item.jd.com/12005808.html', '12005808', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('60', '别怕，Excel VBA其实很简单（第2版）', '45.70', '59.00', '北京大学出版社', 'http://item.jd.com/11974962.html', '11974962', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('61', '别告诉我你懂PPT：全新升级版', '27.20', '42.00', '湖南文艺出版社', 'http://item.jd.com/11807158.html', '11807158', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('62', '设计模式：可复用面向对象软件的基础', '28.90', '35.00', '机械工业出版社', 'http://item.jd.com/10057319.html', '10057319', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('63', 'O\'Reilly：Head First Java（中文版 第2版 涵盖Java5 ...', '52.90', '79.00', '中国电力出版社', 'http://item.jd.com/10100190.html', '10100190', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('64', '编码：隐匿在计算机软硬件背后的语言', '48.20', '59.00', '电子工业出版社', 'http://item.jd.com/11116026.html', '11116026', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('65', 'Spring+MyBatis企业应用实战', '46.30', '58.00', '电子工业出版社', 'http://item.jd.com/12111732.html', '12111732', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('66', '轻量级Java EE企业应用实战：Struts2+Spring4+Hiberna ...', '86.10', '108.00', '电子工业出版社', 'http://item.jd.com/11559101.html', '11559101', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('67', '高性能MySQL（第3版）', '104.60', '128.00', '电子工业出版社', 'http://item.jd.com/11220393.html', '11220393', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('68', '大话设计模式', '37.30', '45.00', '清华大学出版社', 'http://item.jd.com/10079261.html', '10079261', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('69', 'Spring实战（第4版） ', '72.70', '89.00', '人民邮电出版社', 'http://item.jd.com/11899370.html', '11899370', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('70', 'Spring源码深度解析', '56.40', '69.00', '人民邮电出版社', 'http://item.jd.com/11311737.html', '11311737', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('71', '软件开发视频大讲堂：Android从入门到精通（附光盘1张）', '59.30', '69.80', '清华大学出版社', 'http://item.jd.com/11078112.html', '11078112', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('72', '机器学习实战 ', '56.40', '69.00', '人民邮电出版社', 'http://item.jd.com/11242112.html', '11242112', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('73', '机器学习系统设计', '39.10', '49.00', '人民邮电出版社', 'http://item.jd.com/11482400.html', '11482400', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('74', 'Docker开发实践', '47.10', '59.00', '人民邮电出版社', 'http://item.jd.com/11717902.html', '11717902', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('75', 'Docker源码分析', '48.70', '59.00', '机械工业出版社', 'http://item.jd.com/11742113.html', '11742113', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('76', '用户体验要素：以用户为中心的产品设计（原书第2版） ', '32.20', '39.00', '机械工业出版社', 'http://item.jd.com/10690653.html', '10690653', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('77', '大话数据结构', '48.90', '59.00', '清华大学出版社', 'http://item.jd.com/10663703.html', '10663703', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('78', '独角兽之路：20款快速爆发且极具潜力的互联网产品深度剖析（全彩）', '63.00', '79.00', '电子工业出版社', 'http://item.jd.com/11933555.html', '11933555', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('79', '编程之美：微软技术面试心得', '32.70', '40.00', '电子工业出版社', 'http://item.jd.com/10066736.html', '10066736', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('80', '数据挖掘 概念与技术（原书第3版） ', '65.20', '79.00', '机械工业出版社', 'http://item.jd.com/11056660.html', '11056660', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('81', 'Hadoop权威指南（第3版 修订版）', '84.20', '99.00', '清华大学出版社', 'http://item.jd.com/11566298.html', '11566298', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('82', '必然 ', '40.90', '58.00', '电子工业出版社', 'http://item.jd.com/11868029.html', '11868029', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('83', '软件开发视频大讲堂：PHP从入门到精通（第3版 附光盘）', '59.30', '69.80', '清华大学出版社', 'http://item.jd.com/11078096.html', '11078096', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('84', '华章专业开发者丛书・Java并发编程实战 ', '56.90', '69.00', '机械工业出版社', 'http://item.jd.com/10922250.html', '10922250', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('85', 'Photoshop CS6从入门到精通（中文版  附光盘）', '82.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11208733.html', '11208733', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('86', 'Excel 2007应用大全', '82.90', '99.00', '人民邮电出版社', 'http://item.jd.com/10931041.html', '10931041', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('87', '软件开发视频大讲堂：C语言从入门到精通（第2版    附光盘）', '42.30', '49.80', '清华大学出版社', 'http://item.jd.com/11078107.html', '11078107', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('88', 'C语言入门经典（第5版）', '59.30', '69.80', '清华大学出版社', 'http://item.jd.com/11362614.html', '11362614', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('89', 'O\'Reilly：深入理解LINUX内核（第3版）（涵盖2.6版）', '77.40', '98.00', '中国电力出版社', 'http://item.jd.com/10100237.html', '10100237', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('90', 'Effective C++：改善程序与设计的55个具体做法（第3版 中文版）', '53.10', '65.00', '电子工业出版社', 'http://item.jd.com/10393318.html', '10393318', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('91', '黑客与画家：硅谷创业之父Paul Graham文集', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/10582495.html', '10582495', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('92', '华为ICT认证系列丛书：HCNP路由交换实验指南', '74.50', '89.00', '人民邮电出版社', 'http://item.jd.com/11585806.html', '11585806', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('93', '华为ICT认证系列丛书：HCNA网络技术学习指南', '48.20', '59.00', '人民邮电出版社', 'http://item.jd.com/11688335.html', '11688335', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('94', 'HTTP权威指南', '89.10', '109.00', '人民邮电出版社', 'http://item.jd.com/11056556.html', '11056556', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('95', '中文版Photoshop CS6基础培训教程（附光盘）', '29.30', '35.00', '人民邮电出版社', 'http://item.jd.com/11047280.html', '11047280', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('96', 'JavaScript语言精粹（修订版）', '23.90', '49.00', '电子工业出版社', 'http://item.jd.com/11090963.html', '11090963', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('97', 'Excel图表之道：如何制作专业有效的商务图表', '47.10', '59.00', '电子工业出版社', 'http://item.jd.com/10067717.html', '10067717', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('98', '算法(第4版)', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11098789.html', '11098789', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('99', 'Auto CAD 2012中文版从入门到精通（附光盘）', '41.20', '49.90', '中国青年出版社', 'http://item.jd.com/10895439.html', '10895439', null, null, null, null);
INSERT INTO `heat_rankings` VALUES ('100', '术与道 移动应用UI设计必修课', '49.40', '59.00', '人民邮电出版社', 'http://item.jd.com/11889963.html', '11889963', null, null, null, null);

-- ----------------------------
-- Table structure for sales_volume_rankings
-- ----------------------------
DROP TABLE IF EXISTS `sales_volume_rankings`;
CREATE TABLE `sales_volume_rankings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(45) DEFAULT NULL,
  `jd_price` varchar(10) DEFAULT NULL,
  `ding_price` varchar(10) DEFAULT NULL,
  `press` varchar(45) DEFAULT NULL,
  `item_url` varchar(45) DEFAULT NULL,
  `jd_id` varchar(45) DEFAULT NULL,
  `middle_time` varchar(45) DEFAULT NULL,
  `poor_time` varchar(45) DEFAULT NULL,
  `attention_price` varchar(45) DEFAULT NULL,
  `attention` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sales_volume_rankings
-- ----------------------------
INSERT INTO `sales_volume_rankings` VALUES ('1', 'Python编程 从入门到实践 ', '72.70', '89.00', '人民邮电出版社', 'http://item.jd.com/11993134.html', '11993134', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('2', '数学之美（第二版）', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/11572052.html', '11572052', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('3', 'Python从入门到项目实践（全彩版）', '72.40', '99.80', '吉林大学出版社', 'http://item.jd.com/12451724.html', '12451724', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('4', 'Excel 高效办公应用与技巧大全', '50.00', '69.80', '中国水利水电出版社', 'http://item.jd.com/12442347.html', '12442347', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('5', '机器学习【首届京东文学奖-年度新锐入围作品】', '75.10', '88.00', '清华大学出版社', 'http://item.jd.com/11867803.html', '11867803', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('6', 'Java编程思想（第4版） ', '89.10', '108.00', '机械工业出版社', 'http://item.jd.com/10058164.html', '10058164', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('7', '深入理解Java虚拟机：JVM高级特性与最佳实践（第2版）', '65.20', '79.00', '机械工业出版社', 'http://item.jd.com/11252778.html', '11252778', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('8', 'Word Excel PPT 2016办公应用从入门到精通（附光盘）', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/11988251.html', '11988251', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('9', '零基础学C语言（全彩版 附光盘小白手册）', '50.60', '69.80', '吉林大学出版社', 'http://item.jd.com/12250414.html', '12250414', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('10', 'Java从入门到精通（第4版 附光盘）', '57.70', '69.60', '清华大学出版社', 'http://item.jd.com/11985075.html', '11985075', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('11', 'C Primer Plus 第6版 中文版 ', '72.70', '89.00', '人民邮电出版社', 'http://item.jd.com/11917487.html', '11917487', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('12', '零基础学Python（全彩版）', '57.90', '79.80', '吉林大学出版社', 'http://item.jd.com/12353915.html', '12353915', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('13', '鸟哥的Linux私房菜 基础学习篇 第四版', '96.40', '118.00', '人民邮电出版社', 'http://item.jd.com/12443890.html', '12443890', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('14', 'C++ Primer Plus（第6版 中文版） ', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11017238.html', '11017238', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('15', '深度学习 ', '137.30', '168.00', '人民邮电出版社', 'http://item.jd.com/12128543.html', '12128543', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('16', '浪潮之巅 第三版 套装上下册 ', '74.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11922453.html', '11922453', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('17', '和秋叶一起学Word Excel PPT（套装共3册）', '218.20', '267.00', '人民邮电出版社', 'http://item.jd.com/12191631.html', '12191631', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('18', '算法(第4版)', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11098789.html', '11098789', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('19', '深入理解计算机系统（原书第3版） ', '114.70', '139.00', '机械工业出版社', 'http://item.jd.com/12006637.html', '12006637', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('20', 'Photoshop CC从入门到精通PS教程 全彩高清视频版', '71.90', '99.80', '中国水利水电出版社', 'http://item.jd.com/12216067.html', '12216067', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('21', '利用Python进行数据分析（原书第2版） ', '98.20', '119.00', '机械工业出版社', 'http://item.jd.com/12398725.html', '12398725', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('22', 'SQL必知必会 第4版 ', '23.70', '29.00', '人民邮电出版社', 'http://item.jd.com/11232698.html', '11232698', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('23', 'Effective Java中文版（原书第3版）', '98.20', '119.00', '机械工业出版社', 'http://item.jd.com/12507084.html', '12507084', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('24', '企业IT架构转型之道 阿里巴巴中台战略思想与架构实战', '65.20', '79.00', '机械工业出版社', 'http://item.jd.com/12176278.html', '12176278', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('25', '和秋叶一起学Excel', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/12122871.html', '12122871', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('26', 'JavaScript高级程序设计（第3版） ', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/10951037.html', '10951037', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('27', '别怕，Excel VBA其实很简单（第2版）', '45.70', '59.00', '北京大学出版社', 'http://item.jd.com/11974962.html', '11974962', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('28', '零基础学Java（全彩版）（附光盘小白手册）', '50.60', '69.80', '吉林大学出版社', 'http://item.jd.com/12185501.html', '12185501', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('29', 'SQL即查即用 （全彩版）', '36.10', '49.80', '吉林大学出版社', 'http://item.jd.com/12359944.html', '12359944', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('30', '深度学习入门 基于Python的理论与实现', '48.20', '59.00', '人民邮电出版社', 'http://item.jd.com/12403048.html', '12403048', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('31', '代码整洁之道 ', '48.20', '59.00', '人民邮电出版社', 'http://item.jd.com/10064006.html', '10064006', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('32', 'Excel 2016函数与公式应用大全（京东专享签名版）', '92.20', '119.00', '北京大学出版社', 'http://item.jd.com/12479190.html', '12479190', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('33', '设计模式：可复用面向对象软件的基础', '28.90', '35.00', '机械工业出版社', 'http://item.jd.com/10057319.html', '10057319', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('34', '算法图解 ', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/12148832.html', '12148832', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('35', '机器学习实战 ', '56.40', '69.00', '人民邮电出版社', 'http://item.jd.com/11242112.html', '11242112', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('36', '数据结构与算法分析：Java语言描述（原书第3版） ', '56.90', '69.00', '机械工业出版社', 'http://item.jd.com/11886254.html', '11886254', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('37', '人工智能（第2版）', '88.20', '108.00', '人民邮电出版社', 'http://item.jd.com/12401871.html', '12401871', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('38', 'Linux命令行与shell脚本编程大全（第3版） ', '89.10', '109.00', '人民邮电出版社', 'http://item.jd.com/12010266.html', '12010266', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('39', 'PPT设计思维：教你又好又快搞定幻灯片', '48.20', '59.00', '电子工业出版社', 'http://item.jd.com/12061684.html', '12061684', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('40', 'C语言从入门到精通（第3版）（附光盘）/软件开发视频大讲堂', '49.60', '59.80', '清华大学出版社', 'http://item.jd.com/12132428.html', '12132428', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('41', '文明之光（全彩印刷套装1-4册）入选2014中国好书/第六届中华优秀出版物获奖图 ...', '165.00', '246.00', '人民邮电出版社', 'http://item.jd.com/12169220.html', '12169220', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('42', 'Go程序设计语言', '65.20', '79.00', '机械工业出版社', 'http://item.jd.com/12187988.html', '12187988', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('43', '和秋叶一起学PPT 第3版', '72.40', '99.00', '人民邮电出版社', 'http://item.jd.com/12122883.html', '12122883', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('44', 'Python基础教程（第3版）', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/12279949.html', '12279949', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('45', 'Python深度学习', '97.20', '119.00', '人民邮电出版社', 'http://item.jd.com/12409581.html', '12409581', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('46', '数据化管理：洞悉零售及电子商务运营 ', '48.90', '59.90', '电子工业出版社', 'http://item.jd.com/11482086.html', '11482086', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('47', '重构 改善既有代码的设计 ', '56.40', '69.00', '人民邮电出版社', 'http://item.jd.com/11728740.html', '11728740', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('48', '硅谷之谜：浪潮之巅 续集', '39.60', '59.00', '人民邮电出版社', 'http://item.jd.com/11807307.html', '11807307', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('49', 'AutoCAD2018从入门到精通CAD教程 实战案例视频版', '48.10', '69.80', '中国水利水电出版社', 'http://item.jd.com/12184539.html', '12184539', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('50', 'Linux就该这么学', '64.50', '79.00', '人民邮电出版社', 'http://item.jd.com/12269260.html', '12269260', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('51', '零基础学C#（全彩版 附光盘 小白实战手册）', '57.90', '79.80', '吉林大学出版社', 'http://item.jd.com/12271986.html', '12271986', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('52', '笨办法学Python 3', '48.20', '59.00', '人民邮电出版社', 'http://item.jd.com/12372646.html', '12372646', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('53', 'Photoshop CS6从入门到精通PS教程（全彩印 高清视频版）', '71.40', '99.80', '中国水利水电出版社', 'http://item.jd.com/12371603.html', '12371603', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('54', 'MySQL必知必会 ', '31.90', '39.00', '人民邮电出版社', 'http://item.jd.com/10063118.html', '10063118', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('55', '程序员的自我修养：链接、装载与库 ', '53.10', '65.00', '电子工业出版社', 'http://item.jd.com/10067200.html', '10067200', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('56', '算法导论（原书第3版）/计算机科学丛书', '105.60', '128.00', '机械工业出版社', 'http://item.jd.com/11144230.html', '11144230', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('57', 'C语言精彩编程200例（全彩版 附光盘）', '57.90', '79.80', '吉林大学出版社', 'http://item.jd.com/12199075.html', '12199075', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('58', '从零开始学架构：照着做，你也能成为架构师', '80.90', '99.00', '电子工业出版社', 'http://item.jd.com/12450348.html', '12450348', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('59', '我的第一本算法书', '56.40', '69.00', '人民邮电出版社', 'http://item.jd.com/12451331.html', '12451331', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('60', 'O\'Reilly：Head First设计模式（中文版）', '67.60', '98.00', '中国电力出版社', 'http://item.jd.com/10100236.html', '10100236', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('61', '大数据架构详解：从数据获取到深度学习 ', '56.40', '69.00', '电子工业出版社', 'http://item.jd.com/12052744.html', '12052744', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('62', 'Java项目开发实战入门（全彩版）', '37.40', '59.80', '吉林大学出版社', 'http://item.jd.com/12163091.html', '12163091', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('63', '剑指Offer：名企面试官精讲典型编程题（第2版）', '53.10', '65.00', '电子工业出版社', 'http://item.jd.com/12163054.html', '12163054', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('64', 'Java精彩编程200例（全彩版）', '57.90', '79.80', '吉林大学出版社', 'http://item.jd.com/12185937.html', '12185937', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('65', 'Python核心编程（第3版） ', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/11936238.html', '11936238', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('66', 'Python编程快速上手 让繁琐工作自动化', '56.40', '69.00', '人民邮电出版社', 'http://item.jd.com/11943853.html', '11943853', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('67', '网络是怎样连接的', '40.00', '49.00', '人民邮电出版社', 'http://item.jd.com/12109464.html', '12109464', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('68', 'C语言项目开发实战入门（全彩版）', '43.40', '59.80', '吉林大学出版社', 'http://item.jd.com/12163145.html', '12163145', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('69', '大数据之路 阿里巴巴大数据实践 ', '64.50', '79.00', '电子工业出版社', 'http://item.jd.com/12105759.html', '12105759', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('70', 'Vue.js实战', '65.50', '79.00', '清华大学出版社', 'http://item.jd.com/12215519.html', '12215519', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('71', 'TensorFlow：实战Google深度学习框架（第2版）', '72.70', '89.00', '电子工业出版社', 'http://item.jd.com/12287533.html', '12287533', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('72', '深入浅出Spring Boot 2.x', '80.90', '99.00', '人民邮电出版社', 'http://item.jd.com/12403128.html', '12403128', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('73', '美团机器学习实践', '64.50', '79.00', '人民邮电出版社', 'http://item.jd.com/12414240.html', '12414240', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('74', 'Docker技术入门与实战（第3版）', '73.40', '89.00', '机械工业出版社', 'http://item.jd.com/12453318.html', '12453318', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('75', '用户体验要素：以用户为中心的产品设计（原书第2版） ', '32.20', '39.00', '机械工业出版社', 'http://item.jd.com/10690653.html', '10690653', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('76', '高性能MySQL（第3版）', '104.60', '128.00', '电子工业出版社', 'http://item.jd.com/11220393.html', '11220393', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('77', 'C++ Primer（中文版 第5版）', '104.60', '128.00', '电子工业出版社', 'http://item.jd.com/11306138.html', '11306138', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('78', 'Spring实战（第4版） ', '72.70', '89.00', '人民邮电出版社', 'http://item.jd.com/11899370.html', '11899370', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('79', 'HTML5+CSS3+JavaScript从入门到精通（标准版）', '61.90', '89.80', '中国水利水电出版社', 'http://item.jd.com/12123529.html', '12123529', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('80', 'SQL基础教程 第2版', '64.50', '79.00', '人民邮电出版社', 'http://item.jd.com/12212242.html', '12212242', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('81', '六西格玛管理统计指南――MINTAB使用指导（第3版）（中国质量协会六西格玛黑带 ...', '75.40', '89.00', '中国人民大学出版社', 'http://item.jd.com/12367987.html', '12367987', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('82', '百面机器学习 算法工程师带你去面试', '72.70', '89.00', '人民邮电出版社', 'http://item.jd.com/12401859.html', '12401859', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('83', 'Kubernetes in Action中文版', '120.90', '148.00', '电子工业出版社', 'http://item.jd.com/12510666.html', '12510666', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('84', 'O\'Reilly：Head First Java（中文版 第2版 涵盖Java5 ...', '52.90', '79.00', '中国电力出版社', 'http://item.jd.com/10100190.html', '10100190', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('85', '深入浅出数据分析', '71.90', '88.00', '电子工业出版社', 'http://item.jd.com/11127959.html', '11127959', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('86', '结网@改变世界的互联网产品经理（修订版）', '46.30', '69.00', '人民邮电出版社', 'http://item.jd.com/11237904.html', '11237904', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('87', '编码：隐匿在计算机软硬件背后的语言', '48.20', '59.00', '电子工业出版社', 'http://item.jd.com/11116026.html', '11116026', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('88', '图解HTTP+图解TCP/IP+图解网络硬件（套装共3册）', '125.40', '187.00', '人民邮电出版社', 'http://item.jd.com/11519010.html', '11519010', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('89', '新手学电脑从入门到精通（Windows 10+Office 2016版）', '53.50', '69.00', '北京大学出版社', 'http://item.jd.com/11937555.html', '11937555', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('90', 'Java核心技术 卷I：基础知识（原书第10版） ', '98.20', '119.00', '机械工业出版社', 'http://item.jd.com/12037418.html', '12037418', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('91', '第一行代码 Android 第2版 ', '64.50', '79.00', '人民邮电出版社', 'http://item.jd.com/12012505.html', '12012505', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('92', 'Java EE互联网轻量级框架整合开发 SSM框架（Spring MVC+Spr ...', '97.20', '119.00', '电子工业出版社', 'http://item.jd.com/12122571.html', '12122571', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('93', 'SQL Server 从入门到精通（第2版）（配光盘）（软件开发视频大讲堂）', '66.20', '79.80', '清华大学出版社', 'http://item.jd.com/12165847.html', '12165847', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('94', 'Word/Excel/PPT 2016三合一完全自学教程', '68.30', '99.00', '北京大学出版社', 'http://item.jd.com/12273032.html', '12273032', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('95', '零基础学Android （全彩版 附2张光盘小白实战手册）', '65.10', '89.80', '吉林大学出版社', 'http://item.jd.com/12199033.html', '12199033', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('96', 'Excel2016应用大全', '101.10', '128.00', '北京大学出版社', 'http://item.jd.com/12271043.html', '12271043', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('97', 'Scratch 2.0少儿游戏趣味编程', '56.40', '69.00', '人民邮电出版社', 'http://item.jd.com/12360075.html', '12360075', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('98', 'Spring Cloud与Docker微服务架构实战（第2版）', '64.50', '79.00', '电子工业出版社', 'http://item.jd.com/12393837.html', '12393837', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('99', '游戏剧本怎么写', '48.20', '59.00', '人民邮电出版社', 'http://item.jd.com/12417735.html', '12417735', null, null, null, null);
INSERT INTO `sales_volume_rankings` VALUES ('100', '小程序改变一切', '25.70', '42.00', '台海出版社', 'http://item.jd.com/12427026.html', '12427026', null, null, null, null);

-- ----------------------------
-- Table structure for to_sql_demo
-- ----------------------------
DROP TABLE IF EXISTS `to_sql_demo`;
CREATE TABLE `to_sql_demo` (
  `index` bigint(20) DEFAULT NULL,
  `A` bigint(20) DEFAULT NULL,
  `B` bigint(20) DEFAULT NULL,
  `C` bigint(20) DEFAULT NULL,
  KEY `ix_to_sql_demo_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of to_sql_demo
-- ----------------------------
