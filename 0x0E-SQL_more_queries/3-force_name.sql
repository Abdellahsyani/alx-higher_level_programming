-- 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
-- creates the table force_name
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
