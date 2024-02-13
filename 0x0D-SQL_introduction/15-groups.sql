-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- show how many time a score is scored
SELECT score, COUNT(score) AS `number`
  FROM second_table
 GROUP BY score
 ORDER BY score DESC;
