-- 6-states.sql | mysql -hlocalhost -uroot -p
-- create databases and table
CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256)
	);
