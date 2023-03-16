-- List all the cities in the database
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON state_id = cities.states.id
