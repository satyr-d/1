/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 5.6.24 : Database - 学生
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`学生` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `学生`;

/*Table structure for table `学生表` */

DROP TABLE IF EXISTS `学生表`;

CREATE TABLE `学生表` (
  `Sno` char(4) NOT NULL,
  `Sn` char(8) NOT NULL,
  `Sex` char(2) NOT NULL,
  `Age` int(11) DEFAULT NULL,
  `Dept` int(11) NOT NULL,
  PRIMARY KEY (`Sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `学生表` */

insert  into `学生表`(`Sno`,`Sn`,`Sex`,`Age`,`Dept`) values 
('S1','徐啸','女',17,2),
('S2','辛国华','男',18,6),
('S3','徐玮','女',20,1),
('S4','邓一鸥','男',23,6),
('S5','张激扬','男',19,6),
('S6','张辉','女',22,3),
('S7','王克华','男',18,6),
('S8','王刃','男',19,3);

/*Table structure for table `学生选课表` */

DROP TABLE IF EXISTS `学生选课表`;

CREATE TABLE `学生选课表` (
  `sno` char(4) NOT NULL,
  `cno` char(4) NOT NULL DEFAULT '',
  `grade` int(11) DEFAULT NULL,
  PRIMARY KEY (`sno`,`cno`),
  KEY `FK_课程表_学生选课表` (`cno`),
  CONSTRAINT `FK_学生表_学生选课表` FOREIGN KEY (`sno`) REFERENCES `学生表` (`Sno`),
  CONSTRAINT `FK_课程表_学生选课表` FOREIGN KEY (`cno`) REFERENCES `课程表` (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `学生选课表` */

insert  into `学生选课表`(`sno`,`cno`,`grade`) values 
('S1','C1',80),
('S1','C2',85),
('S1','C4',56),
('S1','C5',90),
('S1','C6',75),
('S2','C1',47),
('S2','C3',80),
('S2','C4',75),
('S2','C5',70),
('S3','C1',76),
('S3','C2',70),
('S3','C3',85),
('S3','C4',86),
('S3','C5',90),
('S3','C6',99),
('S4','C1',83),
('S4','C2',85),
('S4','C3',83),
('S5','C2',99),
('S6','C1',96),
('S6','C2',80),
('S6','C3',87);

/*Table structure for table `课程表` */

DROP TABLE IF EXISTS `课程表`;

CREATE TABLE `课程表` (
  `cno` char(4) NOT NULL,
  `cn` char(19) NOT NULL,
  PRIMARY KEY (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `课程表` */

insert  into `课程表`(`cno`,`cn`) values 
('C1','数学'),
('C2','英语'),
('C3','Fortran77'),
('C4','Pascal'),
('C5','政治'),
('C6','物理'),
('C7','逻辑');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
