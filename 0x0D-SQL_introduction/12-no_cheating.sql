-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- change the score of Bob to 10
UPDATE second_table
   SET score = 10
 WHERE name = "Bob";
