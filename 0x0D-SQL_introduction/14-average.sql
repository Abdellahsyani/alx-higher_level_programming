-- usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>
-- show the average of all scores
SELECT AVG(score) AS `average`
  FROM second_table;
