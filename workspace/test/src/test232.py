table ="dsfa"
create_sql=( "CREATE TABLE `%s` (\
	`PROD_INST_ID` varchar(255) DEFAULT NULL,\
	`CUST_ID` varchar(255) DEFAULT NULL,\
	`LATN` varchar(255) DEFAULT NULL,\
            `BUSI_NBR` varchar(255) DEFAULT NULL,\
            `USER_NAME` varchar(255) DEFAULT NULL,\
            `CUST_NAME` varchar(255) DEFAULT NULL,\
            `INSTALL_ADDR` varchar(255) DEFAULT NULL,\
            `CERTIFICATES_NBR` varchar(20) DEFAULT NULL,\
            `mod_time` datetime DEFAULT NULL\
            ENGINE=MyISAM DEFAULT CHARSET=utf8;" % table)
print create_sql