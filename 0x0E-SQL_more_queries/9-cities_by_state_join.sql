--  9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
-- lists all the contained in the database
SELECT cities.name, cities.id, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY id;
