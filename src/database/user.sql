CREATE USER 'ls_user'@'localhost' IDENTIFIED BY 'ls_password';

GRANT ALL PRIVILEGES ON * . * TO 'ls_user'@'localhost';

FLUSH PRIVILEGES;

CREATE DATABASE ls_db CHARACTER SET utf8 COLLATE utf8_general_ci;

USE ls_db;

CREATE TABLE IF NOT EXISTS tbl_clv_prediction (
  id INT(11) NOT NULL AUTO_INCREMENT,
  customer_id VARCHAR(45) DEFAULT NULL,
  max_number_item INT(11) NOT NULL DEFAULT 0,
  max_revenue FLOAT NOT NULL DEFAULT 0,
  total_revenue FLOAT NOT NULL DEFAULT 0,
  total_orders INT(11) NOT NULL DEFAULT 0,
  days_since_last_order INT(11) NOT NULL DEFAULT 0,
  longest_interval INT(11) NOT NULL DEFAULT 0,
  predicted_clv FLOAT NOT NULL DEFAULT 0,
  PRIMARY KEY (id)
) ENGINE=InnoDB;