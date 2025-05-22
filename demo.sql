/*
 Navicat Premium Data Transfer

 Source Server         : 1
 Source Server Type    : MySQL
 Source Server Version : 80100
 Source Host           : localhost:3306
 Source Schema         : demo

 Target Server Type    : MySQL
 Target Server Version : 80100
 File Encoding         : 65001

 Date: 30/12/2024 11:08:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES (2, '员工');
INSERT INTO `auth_group` VALUES (1, '管理员');

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 31 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES (1, 1, 1);
INSERT INTO `auth_group_permissions` VALUES (2, 1, 2);
INSERT INTO `auth_group_permissions` VALUES (3, 1, 3);
INSERT INTO `auth_group_permissions` VALUES (4, 1, 4);
INSERT INTO `auth_group_permissions` VALUES (5, 1, 5);
INSERT INTO `auth_group_permissions` VALUES (6, 1, 6);
INSERT INTO `auth_group_permissions` VALUES (7, 1, 7);
INSERT INTO `auth_group_permissions` VALUES (8, 1, 8);
INSERT INTO `auth_group_permissions` VALUES (9, 1, 9);
INSERT INTO `auth_group_permissions` VALUES (10, 1, 10);
INSERT INTO `auth_group_permissions` VALUES (11, 1, 11);
INSERT INTO `auth_group_permissions` VALUES (12, 1, 12);
INSERT INTO `auth_group_permissions` VALUES (13, 1, 13);
INSERT INTO `auth_group_permissions` VALUES (14, 1, 14);
INSERT INTO `auth_group_permissions` VALUES (15, 1, 15);
INSERT INTO `auth_group_permissions` VALUES (16, 1, 16);
INSERT INTO `auth_group_permissions` VALUES (17, 1, 17);
INSERT INTO `auth_group_permissions` VALUES (18, 1, 18);
INSERT INTO `auth_group_permissions` VALUES (19, 1, 19);
INSERT INTO `auth_group_permissions` VALUES (20, 1, 20);
INSERT INTO `auth_group_permissions` VALUES (21, 1, 21);
INSERT INTO `auth_group_permissions` VALUES (22, 1, 22);
INSERT INTO `auth_group_permissions` VALUES (23, 1, 23);
INSERT INTO `auth_group_permissions` VALUES (24, 1, 24);
INSERT INTO `auth_group_permissions` VALUES (25, 2, 4);
INSERT INTO `auth_group_permissions` VALUES (26, 2, 8);
INSERT INTO `auth_group_permissions` VALUES (27, 2, 12);
INSERT INTO `auth_group_permissions` VALUES (28, 2, 16);
INSERT INTO `auth_group_permissions` VALUES (29, 2, 20);
INSERT INTO `auth_group_permissions` VALUES (30, 2, 24);

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$870000$4Mz7Q1ijEtBRFsaExCWSWH$xWdPYd+WjbrnOwQdTNcBBfcCagANghcd6+xb0Lafpq8=', '2024-12-30 02:20:38.873944', 1, 'admin', '', '', '1530161642@qq.com', 1, 1, '2024-12-03 11:55:00.000000');
INSERT INTO `auth_user` VALUES (2, 'pbkdf2_sha256$870000$Xplm18NYepe8PnVZprDNL5$z/5/jsQyaX4XOcJa6nHw0BWNZD/xSNj7+5HD8L7+aQo=', '2024-12-30 02:22:25.223580', 0, 'a', '', '', '', 0, 1, '2024-12-03 12:32:00.000000');
INSERT INTO `auth_user` VALUES (3, 'pbkdf2_sha256$870000$q6eI3hlEUkj3XTEAX5rhPt$WTv8cqc32sPHudCCAvwRlajQEW8vgNSiEkv1t+jU79Q=', '2024-12-20 09:00:33.212865', 0, 'b', '', '', '', 0, 1, '2024-12-07 06:09:00.000000');
INSERT INTO `auth_user` VALUES (4, 'pbkdf2_sha256$870000$rLJALjdxIzJwGITxHtVkbQ$wMZ6+tjcC99v/Q8dMxk6nM+Uc2EzaH9tUJiFECjQaX8=', NULL, 0, 'c', '', '', '', 0, 1, '2024-12-20 12:45:36.427575');
INSERT INTO `auth_user` VALUES (6, 'pbkdf2_sha256$870000$YX8MOnJmeazsfdGPc6t2mk$2zgKC3VcTGjJPuW76Yd65x2K3uw9J+JGCVHNhY52It0=', NULL, 0, 'd', '', '', '', 0, 1, '2024-12-20 12:46:07.505050');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
INSERT INTO `auth_user_groups` VALUES (1, 1, 1);

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
INSERT INTO `auth_user_user_permissions` VALUES (1, 1, 1);
INSERT INTO `auth_user_user_permissions` VALUES (2, 1, 2);
INSERT INTO `auth_user_user_permissions` VALUES (3, 1, 3);
INSERT INTO `auth_user_user_permissions` VALUES (4, 1, 4);
INSERT INTO `auth_user_user_permissions` VALUES (5, 1, 5);
INSERT INTO `auth_user_user_permissions` VALUES (6, 1, 6);
INSERT INTO `auth_user_user_permissions` VALUES (7, 1, 7);
INSERT INTO `auth_user_user_permissions` VALUES (8, 1, 8);
INSERT INTO `auth_user_user_permissions` VALUES (9, 1, 9);
INSERT INTO `auth_user_user_permissions` VALUES (10, 1, 10);
INSERT INTO `auth_user_user_permissions` VALUES (11, 1, 11);
INSERT INTO `auth_user_user_permissions` VALUES (12, 1, 12);
INSERT INTO `auth_user_user_permissions` VALUES (13, 1, 13);
INSERT INTO `auth_user_user_permissions` VALUES (14, 1, 14);
INSERT INTO `auth_user_user_permissions` VALUES (15, 1, 15);
INSERT INTO `auth_user_user_permissions` VALUES (16, 1, 16);
INSERT INTO `auth_user_user_permissions` VALUES (17, 1, 17);
INSERT INTO `auth_user_user_permissions` VALUES (18, 1, 18);
INSERT INTO `auth_user_user_permissions` VALUES (19, 1, 19);
INSERT INTO `auth_user_user_permissions` VALUES (20, 1, 20);
INSERT INTO `auth_user_user_permissions` VALUES (21, 1, 21);
INSERT INTO `auth_user_user_permissions` VALUES (22, 1, 22);
INSERT INTO `auth_user_user_permissions` VALUES (23, 1, 23);
INSERT INTO `auth_user_user_permissions` VALUES (24, 1, 24);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK (`action_flag` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2024-12-03 12:08:52.432018', '1', '管理员', 1, '[{\"added\": {}}]', 3, 1);
INSERT INTO `django_admin_log` VALUES (2, '2024-12-03 12:09:28.619457', '2', '员工', 1, '[{\"added\": {}}]', 3, 1);
INSERT INTO `django_admin_log` VALUES (3, '2024-12-12 16:29:51.937903', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"Groups\", \"User permissions\", \"Last login\"]}}]', 4, 1);
INSERT INTO `django_admin_log` VALUES (4, '2024-12-19 10:07:07.937910', '3', 'admin2', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 1);
INSERT INTO `django_admin_log` VALUES (5, '2024-12-19 10:07:14.661062', '3', 'admin2', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 1);
INSERT INTO `django_admin_log` VALUES (6, '2024-12-19 10:08:43.670899', '2', 'admin11', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 1);
INSERT INTO `django_admin_log` VALUES (7, '2024-12-19 10:08:49.183205', '2', 'a', 2, '[{\"changed\": {\"fields\": [\"Username\"]}}]', 4, 1);
INSERT INTO `django_admin_log` VALUES (8, '2024-12-19 10:09:00.543308', '3', 'admin2', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 1);
INSERT INTO `django_admin_log` VALUES (9, '2024-12-19 10:09:06.615181', '3', 'b', 2, '[{\"changed\": {\"fields\": [\"Username\", \"Last login\"]}}]', 4, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2024-12-03 03:18:42.197595');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2024-12-03 03:18:42.529294');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2024-12-03 03:18:42.609781');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2024-12-03 03:18:42.617299');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2024-12-03 03:18:42.622860');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2024-12-03 03:18:42.672423');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2024-12-03 03:18:42.708714');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2024-12-03 03:18:42.726585');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2024-12-03 03:18:42.732586');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2024-12-03 03:18:42.769662');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2024-12-03 03:18:42.771661');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2024-12-03 03:18:42.777660');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2024-12-03 03:18:42.816542');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2024-12-03 03:18:42.854269');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2024-12-03 03:18:42.869861');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2024-12-03 03:18:42.876890');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2024-12-03 03:18:42.915545');
INSERT INTO `django_migrations` VALUES (18, 'sessions', '0001_initial', '2024-12-03 03:18:54.313319');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('39pwhyfb1bhby62cndrevdhtrpddnyxv', '.eJxVjEEOwiAQRe_C2hAYaJm6dO8ZmhkGpGpKUtqV8e7apAvd_vfef6mRtrWMW0vLOIk6K6tOvxtTfKR5B3Kn-VZ1rPO6TKx3RR-06WuV9Lwc7t9BoVa-dRjQQEAEcd7nbIQBnYTOZ-ys54G6EA1ZQBg4IoqFPjpy5AFYYs_q_QG6BDdC:1tOc18:T4wVbTaNyTTo4O_ocxjiKoZscDcD3uX5UWWpsswS8tE', '2025-01-03 12:22:06.226701');
INSERT INTO `django_session` VALUES ('50qnofd8v5z32pv2470cofknifvuc50y', '.eJxVjEEOwiAUBe_C2hCgYFuX7j0DeXz4UjU0Ke3KeHdp0oVuZ-a9t_DY1uy3mhY_RXERgzj9sgB6prKL-EC5z5Lmsi5TkHsiD1vlbY7pdT3av4OMmtuaVGed0WxUAnGntQukw2AtgmXuRlKN9mceew0FgmFWCBGAaanT4vMF9bY4vw:1tOec0:GxmAuMb_lE8f5MlKwU2h0sHY9jz6SA7QPE8ElSS06gA', '2025-01-03 15:08:20.668089');
INSERT INTO `django_session` VALUES ('e2yufm0igi1mlcxj9echfgos7nesrk1n', '.eJxVjEEOwiAQRe_C2hAYaJm6dO8ZmhkGpGpKUtqV8e7apAvd_vfef6mRtrWMW0vLOIk6K6tOvxtTfKR5B3Kn-VZ1rPO6TKx3RR-06WuV9Lwc7t9BoVa-dRjQQEAEcd7nbIQBnYTOZ-ys54G6EA1ZQBg4IoqFPjpy5AFYYs_q_QG6BDdC:1tNVJU:qYES4G2WQRuBF9fgiC2fmrPGFNbfSTqi-UbLKSbTUkg', '2024-12-31 11:00:28.310816');
INSERT INTO `django_session` VALUES ('g2p5wzopeyrm750vsn3aipubazk2agzo', '.eJxVjEEOwiAQRe_C2hAYaJm6dO8ZmhkGpGpKUtqV8e7apAvd_vfef6mRtrWMW0vLOIk6K6tOvxtTfKR5B3Kn-VZ1rPO6TKx3RR-06WuV9Lwc7t9BoVa-dRjQQEAEcd7nbIQBnYTOZ-ys54G6EA1ZQBg4IoqFPjpy5AFYYs_q_QG6BDdC:1tOeZv:AwSTFNDG1yijP_EePpP9e2aBQMgGP4ALfzvWsut146A', '2025-01-03 15:06:11.250881');
INSERT INTO `django_session` VALUES ('mdwausvafhi4t1jgd7ird39zgdyr23s3', '.eJxVjEEOwiAQRe_C2hAYaJm6dO8ZmhkGpGpKUtqV8e7apAvd_vfef6mRtrWMW0vLOIk6K6tOvxtTfKR5B3Kn-VZ1rPO6TKx3RR-06WuV9Lwc7t9BoVa-dRjQQEAEcd7nbIQBnYTOZ-ys54G6EA1ZQBg4IoqFPjpy5AFYYs_q_QG6BDdC:1tOY73:oRebdaoDGNTdGgsjjnLBtEtRXlL37Xsm7jz4J-TJNMs', '2025-01-03 08:11:57.193869');
INSERT INTO `django_session` VALUES ('oxhbm9qw4gpfktv9v4aspkh60xhbq1j8', '.eJxVjEEOwiAQRe_C2hAYaJm6dO8ZmhkGpGpKUtqV8e7apAvd_vfef6mRtrWMW0vLOIk6K6tOvxtTfKR5B3Kn-VZ1rPO6TKx3RR-06WuV9Lwc7t9BoVa-dRjQQEAEcd7nbIQBnYTOZ-ys54G6EA1ZQBg4IoqFPjpy5AFYYs_q_QG6BDdC:1tOYic:QNhBw_XeyDK1H287ObzuQv1q5wsFsziu3pKBRSnA7DU', '2025-01-03 08:50:46.516025');
INSERT INTO `django_session` VALUES ('vx3ok11dgumc0j8boclinneae4th7qod', '.eJxVjEEOwiAQRe_C2hAYaJm6dO8ZmhkGpGpKUtqV8e7apAvd_vfef6mRtrWMW0vLOIk6K6tOvxtTfKR5B3Kn-VZ1rPO6TKx3RR-06WuV9Lwc7t9BoVa-dRjQQEAEcd7nbIQBnYTOZ-ys54G6EA1ZQBg4IoqFPjpy5AFYYs_q_QG6BDdC:1tOV89:6mqHy2mEDeQjqxUsICeEXUuOL39qDpNPL5dMbvGGAow', '2025-01-03 05:00:53.221978');

-- ----------------------------
-- Table structure for employee_attendance
-- ----------------------------
DROP TABLE IF EXISTS `employee_attendance`;
CREATE TABLE `employee_attendance`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `month` int NOT NULL,
  `employee_id` int NULL DEFAULT NULL,
  `department_id` int NULL DEFAULT NULL,
  `late_days` int NULL DEFAULT 0,
  `early_leave_days` int NULL DEFAULT 0,
  `leave_days` int NULL DEFAULT 0,
  `overtime_hours` float NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `employee_id`(`employee_id` ASC) USING BTREE,
  INDEX `department_id`(`department_id` ASC) USING BTREE,
  CONSTRAINT `employee_attendance_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_employee` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `employee_attendance_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `employee_department` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employee_attendance
-- ----------------------------
INSERT INTO `employee_attendance` VALUES (1, 2024, 11, 1, 1, 2, 1, 0, 3);
INSERT INTO `employee_attendance` VALUES (2, 2024, 11, 2, 1, 0, 0, 2, 10);
INSERT INTO `employee_attendance` VALUES (3, 2024, 11, 3, 2, 1, 1, 0, 8);
INSERT INTO `employee_attendance` VALUES (4, 2024, 11, 4, 3, 0, 1, 1, 6);
INSERT INTO `employee_attendance` VALUES (5, 2024, 11, 5, 1, 3, 0, 0, 12);
INSERT INTO `employee_attendance` VALUES (6, 2024, 11, 6, 4, 0, 0, 1, 15);
INSERT INTO `employee_attendance` VALUES (7, 2024, 11, 7, 5, 1, 2, 0, 3);
INSERT INTO `employee_attendance` VALUES (8, 2024, 11, 8, 4, 0, 0, 2, 9);
INSERT INTO `employee_attendance` VALUES (9, 2024, 11, 9, 3, 1, 1, 0, 7);

-- ----------------------------
-- Table structure for employee_department
-- ----------------------------
DROP TABLE IF EXISTS `employee_department`;
CREATE TABLE `employee_department`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employee_department
-- ----------------------------
INSERT INTO `employee_department` VALUES (1, '技术部');
INSERT INTO `employee_department` VALUES (2, '人力资源部');
INSERT INTO `employee_department` VALUES (3, '财务部');
INSERT INTO `employee_department` VALUES (4, '市场部');
INSERT INTO `employee_department` VALUES (5, '行政部');

-- ----------------------------
-- Table structure for employee_employee
-- ----------------------------
DROP TABLE IF EXISTS `employee_employee`;
CREATE TABLE `employee_employee`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `supervisor_id` int NULL DEFAULT NULL,
  `department_id` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `department_id`(`department_id` ASC) USING BTREE,
  INDEX `fk_supervisor`(`supervisor_id` ASC) USING BTREE,
  CONSTRAINT `employee_employee_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `employee_department` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_supervisor` FOREIGN KEY (`supervisor_id`) REFERENCES `employee_employee` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employee_employee
-- ----------------------------
INSERT INTO `employee_employee` VALUES (1, '张三', NULL, 1);
INSERT INTO `employee_employee` VALUES (2, '李四', 1, 1);
INSERT INTO `employee_employee` VALUES (3, '王五', 1, 2);
INSERT INTO `employee_employee` VALUES (4, '赵六', 1, 3);
INSERT INTO `employee_employee` VALUES (5, '钱七', 2, 1);
INSERT INTO `employee_employee` VALUES (6, '孙八', 3, 4);
INSERT INTO `employee_employee` VALUES (7, '周九', 1, 5);
INSERT INTO `employee_employee` VALUES (8, '吴十', 2, 4);
INSERT INTO `employee_employee` VALUES (9, '郑十一', 3, 3);

-- ----------------------------
-- Table structure for employee_salary
-- ----------------------------
DROP TABLE IF EXISTS `employee_salary`;
CREATE TABLE `employee_salary`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `month` int NOT NULL,
  `employee_id` int NULL DEFAULT NULL,
  `department_id` int NULL DEFAULT NULL,
  `base_salary` float NULL DEFAULT NULL,
  `housing_allowance` float NULL DEFAULT NULL,
  `gross_salary` float NULL DEFAULT NULL,
  `deductions` float NULL DEFAULT NULL,
  `net_salary` float NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `employee_id`(`employee_id` ASC) USING BTREE,
  INDEX `department_id`(`department_id` ASC) USING BTREE,
  CONSTRAINT `employee_salary_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_employee` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `employee_salary_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `employee_department` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employee_salary
-- ----------------------------
INSERT INTO `employee_salary` VALUES (1, 2024, 11, 1, 1, 9000, 1000, 10060, 150, 9910);
INSERT INTO `employee_salary` VALUES (6, 2024, 11, 7, 5, 3000, 50, 3110, 150, 2960);
INSERT INTO `employee_salary` VALUES (8, 2024, 11, 4, 3, 1000, 2000, 3120, 50, 3070);

-- ----------------------------
-- Table structure for employee_systemconfig
-- ----------------------------
DROP TABLE IF EXISTS `employee_systemconfig`;
CREATE TABLE `employee_systemconfig`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `work_days_per_month` int NULL DEFAULT 22,
  `late_deduction_rate` float NULL DEFAULT 2.5,
  `early_leave_deduction_rate` float NULL DEFAULT 5,
  `leave_deduction_rate` float NULL DEFAULT 5,
  `overtime_bonus_rate` float NULL DEFAULT 1.5,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employee_systemconfig
-- ----------------------------
INSERT INTO `employee_systemconfig` VALUES (1, 22, 50, 50, 50, 20);

-- ----------------------------
-- View structure for department_salary_summary
-- ----------------------------
DROP VIEW IF EXISTS `department_salary_summary`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `department_salary_summary` AS select `d`.`name` AS `department_name`,sum(`es`.`base_salary`) AS `total_base_salary`,sum(`es`.`housing_allowance`) AS `total_housing_allowance`,sum(`es`.`gross_salary`) AS `total_gross_salary`,sum(`es`.`deductions`) AS `total_deductions`,sum(`es`.`net_salary`) AS `total_net_salary` from (`employee_salary` `es` join `employee_department` `d` on((`es`.`department_id` = `d`.`id`))) group by `d`.`name`;

-- ----------------------------
-- Procedure structure for calculate_salary
-- ----------------------------
DROP PROCEDURE IF EXISTS `calculate_salary`;
delimiter ;;
CREATE PROCEDURE `calculate_salary`(IN emp_id INT, IN calc_year INT, IN calc_month INT)
BEGIN
    -- 澹版槑鍙橀噺
    DECLARE base_salary FLOAT;
    DECLARE housing_allowance FLOAT;
    DECLARE late_deduction FLOAT;
    DECLARE early_leave_deduction FLOAT;
    DECLARE leave_deduction FLOAT;
    DECLARE overtime_bonus FLOAT;
    DECLARE total_deduction FLOAT;
    DECLARE final_salary FLOAT;

    DECLARE late_days INT;
    DECLARE early_leave_days INT;
    DECLARE leave_days INT;
    DECLARE overtime_hours FLOAT;

    -- 鑾峰彇鍩虹?宸ヨ祫鍜屼綇鎴胯ˉ璐?    SELECT base_salary, housing_allowance
    INTO base_salary, housing_allowance
    FROM employee_salary
    WHERE employee_id = emp_id AND year = calc_year AND month = calc_month;

    -- 鑾峰彇鎵ｆ?鍜屽姞鐝?巼
    SELECT late_deduction_rate, early_leave_deduction_rate, leave_deduction_rate, overtime_bonus_rate
    INTO late_deduction, early_leave_deduction, leave_deduction, overtime_bonus
    FROM employee_systemconfig
    LIMIT 1;

    -- 鑾峰彇鑰冨嫟鏁版嵁
    SELECT late_days, early_leave_days, leave_days, overtime_hours
    INTO late_days, early_leave_days, leave_days, overtime_hours
    FROM employee_attendance
    WHERE employee_id = emp_id AND year = calc_year AND month = calc_month;

    -- 璁＄畻鎵ｆ?鍜屽姞鐝??閲?    SET late_deduction = late_days * late_deduction;
    SET early_leave_deduction = early_leave_days * early_leave_deduction;
    SET leave_deduction = leave_days * leave_deduction;
    SET overtime_bonus = overtime_hours * overtime_bonus;

    -- 璁＄畻鎬绘墸娆惧拰鏈?粓宸ヨ祫
    SET total_deduction = late_deduction + early_leave_deduction + leave_deduction;
    SET final_salary = base_salary + housing_allowance + overtime_bonus - total_deduction;

    -- 鏇存柊钖?祫琛?    UPDATE employee_salary
    SET gross_salary = base_salary + housing_allowance,
        deductions = total_deduction,
        net_salary = final_salary
    WHERE employee_id = emp_id AND year = calc_year AND month = calc_month;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table employee_systemconfig
-- ----------------------------
DROP TRIGGER IF EXISTS `update_salary_after_system_config_update`;
delimiter ;;
CREATE TRIGGER `update_salary_after_system_config_update` AFTER UPDATE ON `employee_systemconfig` FOR EACH ROW BEGIN
    -- 更新员工薪资
    UPDATE employee_salary es
    JOIN employee_attendance ea
    ON es.employee_id = ea.employee_id AND es.year = ea.year AND es.month = ea.month
    JOIN employee_systemconfig esc ON 1 = 1  -- 连接系统配置表
    SET
        -- 重新计算应发工资和实发工资
        es.gross_salary = es.base_salary + es.housing_allowance + (ea.overtime_hours * esc.overtime_bonus_rate),
        es.deductions = (ea.late_days * esc.late_deduction_rate) +
                        (ea.early_leave_days * esc.early_leave_deduction_rate) +
                        IF(ea.leave_days > 3, (ea.leave_days - 3) * esc.leave_deduction_rate, 0),
        es.net_salary = (es.base_salary + es.housing_allowance + (ea.overtime_hours * esc.overtime_bonus_rate)) -
                        ((ea.late_days * esc.late_deduction_rate) +
                         (ea.early_leave_days * esc.early_leave_deduction_rate) +
                         IF(ea.leave_days > 3, (ea.leave_days - 3) * esc.leave_deduction_rate, 0));

END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
