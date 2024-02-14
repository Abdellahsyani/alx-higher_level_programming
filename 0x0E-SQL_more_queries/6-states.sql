-- 6-states.sql | mysql -hlocalhost -uroot -p
-- create databases and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	name VARCHAR(256)
);
