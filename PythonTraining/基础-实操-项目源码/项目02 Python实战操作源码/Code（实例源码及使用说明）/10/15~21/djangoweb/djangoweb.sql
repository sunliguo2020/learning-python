/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : djangoweb

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-06-01 13:07:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('20', 'Can view session', '5', 'view_session');
INSERT INTO `auth_permission` VALUES ('21', 'Can add 用户', '6', 'add_user');
INSERT INTO `auth_permission` VALUES ('22', 'Can change 用户', '6', 'change_user');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete 用户', '6', 'delete_user');
INSERT INTO `auth_permission` VALUES ('24', 'Can view 用户', '6', 'view_user');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 种类', '7', 'add_type');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 种类', '7', 'change_type');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 种类', '7', 'delete_type');
INSERT INTO `auth_permission` VALUES ('28', 'Can view 种类', '7', 'view_type');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 具体类型', '8', 'add_typedetail');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 具体类型', '8', 'change_typedetail');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 具体类型', '8', 'delete_typedetail');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 具体类型', '8', 'view_typedetail');
INSERT INTO `auth_permission` VALUES ('33', 'Can add poetry', '9', 'add_poetry');
INSERT INTO `auth_permission` VALUES ('34', 'Can change poetry', '9', 'change_poetry');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete poetry', '9', 'delete_poetry');
INSERT INTO `auth_permission` VALUES ('36', 'Can view poetry', '9', 'view_poetry');

-- ----------------------------
-- Table structure for `df_type`
-- ----------------------------
DROP TABLE IF EXISTS `df_type`;
CREATE TABLE `df_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_type
-- ----------------------------
INSERT INTO `df_type` VALUES ('1', '2019-05-30 14:16:40.000000', '2019-05-30 14:16:44.000000', '0', '吉林省');
INSERT INTO `df_type` VALUES ('2', '2019-05-30 14:17:31.000000', '2019-05-30 14:17:28.000000', '0', '江苏省');

-- ----------------------------
-- Table structure for `df_type_detail`
-- ----------------------------
DROP TABLE IF EXISTS `df_type_detail`;
CREATE TABLE `df_type_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_type_detail_type_id_54500392_fk_df_type_id` (`type_id`),
  CONSTRAINT `df_type_detail_type_id_54500392_fk_df_type_id` FOREIGN KEY (`type_id`) REFERENCES `df_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_type_detail
-- ----------------------------
INSERT INTO `df_type_detail` VALUES ('1', '2019-05-30 14:18:11.000000', '2019-05-30 14:18:15.000000', '0', '长春市', '1');
INSERT INTO `df_type_detail` VALUES ('2', '2019-05-30 14:18:31.000000', '2019-05-30 14:18:36.000000', '0', '吉林市', '1');
INSERT INTO `df_type_detail` VALUES ('3', '2019-05-30 14:19:11.000000', '2019-05-30 14:19:16.000000', '0', '苏州市', '2');
INSERT INTO `df_type_detail` VALUES ('4', '2019-05-30 14:19:42.000000', '2019-05-30 14:19:45.000000', '0', '南京市', '2');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_mail_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_mail_user_id` FOREIGN KEY (`user_id`) REFERENCES `mail_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('7', 'ajax', 'type');
INSERT INTO `django_content_type` VALUES ('8', 'ajax', 'typedetail');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'mail', 'user');
INSERT INTO `django_content_type` VALUES ('9', 'search', 'poetry');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-05-30 06:16:02.274523');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2019-05-30 06:16:02.393455');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2019-05-30 06:16:02.491398');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2019-05-30 06:16:02.778236');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2019-05-30 06:16:02.785231');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2019-05-30 06:16:02.792227');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2019-05-30 06:16:02.800223');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2019-05-30 06:16:02.803224');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2019-05-30 06:16:02.809217');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2019-05-30 06:16:02.816213');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2019-05-30 06:16:02.823210');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0010_alter_group_name_max_length', '2019-05-30 06:16:02.932147');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0011_update_proxy_permissions', '2019-05-30 06:16:02.941142');
INSERT INTO `django_migrations` VALUES ('14', 'mail', '0001_initial', '2019-05-30 06:16:03.036088');
INSERT INTO `django_migrations` VALUES ('15', 'admin', '0001_initial', '2019-05-30 06:16:03.351908');
INSERT INTO `django_migrations` VALUES ('16', 'admin', '0002_logentry_remove_auto_add', '2019-05-30 06:16:03.482832');
INSERT INTO `django_migrations` VALUES ('17', 'admin', '0003_logentry_add_action_flag_choices', '2019-05-30 06:16:03.493826');
INSERT INTO `django_migrations` VALUES ('18', 'ajax', '0001_initial', '2019-05-30 06:16:03.554792');
INSERT INTO `django_migrations` VALUES ('19', 'ajax', '0002_auto_20190530_1406', '2019-05-30 06:16:03.724695');
INSERT INTO `django_migrations` VALUES ('20', 'mail', '0002_auto_20190530_1406', '2019-05-30 06:16:03.798652');
INSERT INTO `django_migrations` VALUES ('21', 'sessions', '0001_initial', '2019-05-30 06:16:03.893599');
INSERT INTO `django_migrations` VALUES ('22', 'search', '0001_initial', '2019-05-31 08:00:27.269832');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for `mail_user`
-- ----------------------------
DROP TABLE IF EXISTS `mail_user`;
CREATE TABLE `mail_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `phone` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mail_user
-- ----------------------------

-- ----------------------------
-- Table structure for `mail_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `mail_user_groups`;
CREATE TABLE `mail_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mail_user_groups_user_id_group_id_35ce6c3a_uniq` (`user_id`,`group_id`),
  KEY `mail_user_groups_group_id_a4890e73_fk_auth_group_id` (`group_id`),
  CONSTRAINT `mail_user_groups_group_id_a4890e73_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `mail_user_groups_user_id_4eebf452_fk_mail_user_id` FOREIGN KEY (`user_id`) REFERENCES `mail_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mail_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `mail_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `mail_user_user_permissions`;
CREATE TABLE `mail_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mail_user_user_permissions_user_id_permission_id_52c21408_uniq` (`user_id`,`permission_id`),
  KEY `mail_user_user_permi_permission_id_2a9ce862_fk_auth_perm` (`permission_id`),
  CONSTRAINT `mail_user_user_permi_permission_id_2a9ce862_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `mail_user_user_permissions_user_id_1c678589_fk_mail_user_id` FOREIGN KEY (`user_id`) REFERENCES `mail_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mail_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `search_poetry`
-- ----------------------------
DROP TABLE IF EXISTS `search_poetry`;
CREATE TABLE `search_poetry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `author` varchar(20) NOT NULL,
  `detail` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of search_poetry
-- ----------------------------
INSERT INTO `search_poetry` VALUES ('1', '菩萨蛮·平林漠漠烟如织', '李白', '平林漠漠烟如织，寒山一带伤心碧。暝色入高楼，有人楼上愁。\r\n玉阶空伫立，宿鸟归飞急。何处是归程？长亭连短亭。');
INSERT INTO `search_poetry` VALUES ('2', '忆秦娥·箫声咽', '李白', '箫声咽，秦娥梦断秦楼月。秦楼月，年年柳色，灞陵伤别。\r\n乐游原上清秋节，咸阳古道音尘绝。音尘绝，西风残照，汉家陵阙。');
INSERT INTO `search_poetry` VALUES ('3', '定风波', '苏轼', '常羡人间琢玉郎，天应乞与点酥娘。尽道清歌传皓齿，风起，雪飞炎海变清凉。(尽道 一作：自作)\r\n万里归来颜愈少，微笑，笑时犹带岭梅香。试问岭南应不好，却道：此心安处是吾乡。 ');
INSERT INTO `search_poetry` VALUES ('4', '兰陵王·柳', '周邦彦', '柳阴直，烟里丝丝弄碧。隋堤上、曾见几番，拂水飘绵送行色。登临望故国，谁识京华倦客？长亭路，年去岁来，应折柔条过千尺。\r\n闲寻旧踪迹，又酒趁哀弦，灯照离席。梨花榆火催寒食。愁一箭风快，半篙波暖，回头迢递便数驿，望人在天北。\r\n凄恻，恨堆积！渐别浦萦回，津堠岑寂，斜阳冉冉春无极。念月榭携手，露桥闻笛。沉思前事，似梦里，泪暗滴。');
INSERT INTO `search_poetry` VALUES ('5', '卜算子·咏梅', '陆游', '驿外断桥边，寂寞开无主。已是黄昏独自愁，更著风和雨。 \r\n无意苦争春，一任群芳妒。零落成泥碾作尘，只有香如故。 ');
INSERT INTO `search_poetry` VALUES ('6', '卜算子·见也如何暮', '石孝发', '见也如何暮。别也如何遽。别也应难见也难，后会难凭据。 \r\n去也如何去。住也如何住。住也应难去也难，此际难分付。 ');
INSERT INTO `search_poetry` VALUES ('7', '钗头凤·红酥手', '陆游', '红酥手，黄縢酒，满城春色宫墙柳。东风恶，欢情薄。一怀愁绪，几年离索。错、错、错。\r\n春如旧，人空瘦，泪痕红浥鲛绡透。桃花落，闲池阁。山盟虽在，锦书难托。莫、莫、莫！ ');
INSERT INTO `search_poetry` VALUES ('8', '凤凰台上忆吹箫·香冷金猊', '李清照', '香冷金猊，被翻红浪，起来慵自梳头。任宝奁尘满，日上帘钩。生怕离怀别苦，多少事、欲说还休。新来瘦，非干病酒，不是悲秋。\r\n休休，这回去也，千万遍《阳关》，也则难留。念武陵人远，烟锁秦楼。惟有楼前流水，应念我、终日凝眸。凝眸处，从今又添，一段新愁。');
INSERT INTO `search_poetry` VALUES ('9', '小重山·昨夜寒蛩不住鸣', '岳飞', '昨夜寒蛩不住鸣。惊回千里梦，已三更。起来独自绕阶行。人悄悄，帘外月胧明。\r\n白首为功名。旧山松竹老，阻归程。欲将心事付瑶琴。知音少，弦断有谁听。');
INSERT INTO `search_poetry` VALUES ('10', '鹧鸪天·一点残红欲尽时', '周紫芝', '一点残红欲尽时。乍凉秋气满屏帏。梧桐叶上三更雨，叶叶声声是别离。 \r\n调宝瑟，拨金猊。那时同唱鹧鸪词。如今风雨西楼夜，不听清歌也泪垂。 ');
