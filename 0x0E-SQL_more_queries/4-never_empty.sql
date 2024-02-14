-- 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
-- creates the table
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
)
