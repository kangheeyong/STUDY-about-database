# Postgres

## add sample data
- `\i /postgres/sample_data/person.sql;`
- `\i /postgres/sample_data/car.sql;`

## command
### distinct
  - `SELECT DISTINCT country_of_birth FROM person;`
### in
  - `SELECT * FROM person WHERE country_of_birth IN ('China', 'Poland');`
### like
  - `SELECT * FROM person WHERE email LIKE '%.com';`
  - `SELECT * FROM person WHERE email LIKE '________@%';`
### group by
  - `SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth;`
  - `SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth ORDER BY country_of_birth;`
### group by having
  - `SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*) > 5 ORDER BY country_of_birth;`
  - `SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*) > 5 AND COUNT(*) < 10 ORDER BY country_of_birth;`
### calculating min, max & average
  - `SELECT MAX(price) FROM car;`
  - `SELECT MIN(price) FROM car;`
  - `SELECT AVG(price) FROM car;`
  - `SELECT ROUND(AVG(price)) FROM car;`
  - `SELECT maker, model, MIN(price) FROM car GROUP BY maker, model;`
### sum
  - `SELECT SUM(price) FROM car;`
  - `SELECT maker, SUM(price) FROM car GROUP BY maker;`
### round
  - `SELECT *, price * 0.1 FROM car;`
  - `SELECT *, ROUND(price * 0.1, 2), ROUND(price - price * 0.1, 2) FROM car;`
### alias
  - `SELECT *, ROUND(price * 0.1, 2) AS ten_percent, ROUND(price - price * 0.1, 2) AS discount_after_ten_percent FROM car;`
### coalesce
  - `SELECT first_name, COALESCE(email, 'email not provided') AS email FROM person;`

## references
  - https://www.youtube.com/watch?v=qw--VYLpxG4&t=421s
