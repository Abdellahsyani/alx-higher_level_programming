-- usage: 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hb
-- lists all the cities of california
SELECT name
FROM hbtn_0d_usa.cities
WHERE state_id = (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California')
ORDER BY id ASC;
