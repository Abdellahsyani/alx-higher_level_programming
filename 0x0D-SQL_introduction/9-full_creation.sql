-- usgae: 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- create a new table data
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT
	INTO second_table
		(id, name, score)
	VALUES (1, 'john', 10),
	       (2, 'Alex', 2),
	       (3, 'Bob', 14),
	       (4, 'George', 8);
