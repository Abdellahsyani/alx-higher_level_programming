-- usage: 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hb
-- lists all the cities of california
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
