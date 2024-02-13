-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- show all records sorted by score (descending)
SELECT score, name
  FROM second_table
 ORDER BY score DESC;
