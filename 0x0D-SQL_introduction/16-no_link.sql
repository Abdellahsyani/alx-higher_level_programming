-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- list all the records with available name
SELECT score, name
  FROM second_table
 WHERE name IS NOT NULL
 ORDER BY score DESC;
