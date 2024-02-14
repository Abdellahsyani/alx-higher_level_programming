-- 7-cities.sql | mysql -hlocalhost -uroot -p
-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
