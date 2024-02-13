-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- create a new table
SELECT score, name
  FROM second_table
 WHERE score >= 10
 ORDER BY score DESC;
