-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- delete any record with a score less than 5
DELETE
  FROM second_table
 WHERE score <= 5;
