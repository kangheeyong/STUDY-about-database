# Postgres

## add sample data
- `\i /postgres/sample_data/person.sql;`
- `\i /postgres/sample_data/car.sql;`
- `\i /postgres/sample_data/person_car.sql;`

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
  - `SELECT email, COUNT(*) FROM person GROUP BY email HAVING count(*) > 1;`
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
### nullif
  - `SELECT COALESCE(10 / NULLIF(0, 0), 0);`
### timestamps and dates
  - `SELECT NOW();`
  - `SELECT NOW()::DATE;`
  - `SELECT NOW()::TIME;`
  - `SELECT NOW() - INTERVAL '1 YEARS';`
  - `SELECT (NOW() + INTERVAL '1 YEARS')::DATE;`
  - `SELECT EXTRACT(YEAR FROM NOW());`
### age
  - `SELECT *, AGE(NOW(), date_of_birth) AS age FROM person;`
### add & drop pkey
  - `ALTER TABLE person ADD PRIMARY KEY (id);`
  - `ALTER TABLE person DROP CONSTRAINT person_pkey;`
### add & drop constraint unique
  - `ALTER TABLE person ADD CONSTRAINT unique_email_address UNIQUE (email);`
  - `ALTER TABLE person ADD UNIQUE (email);`
  - `ALTER TABLE person DROP CONSTRAINT unique_email_address;`
### check constraint
  - `ALTER TABLE person ADD CONSTRAINT gender_constrain CHECK (gender IN ('Female', 'Genderqueer', 'Bigender', 'Male', 'Polygender', 'Non-binary', 'Agender', 'Genderfluid'));`
### delete recode
  - `DELETE FROM person WHERE id = 1;`
### update recode
  - `UPDATE person SET email = 'jeiger@namve.com' WHERE id = 3;`
### on conflict
  - `INSERT INTO person (id, first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES (4, 'Flo', 'Sexcey', 'fsexcey3@seesaa.net', 'Bigender', '2021-05-22', 'Honduras') ON CONFLICT (id) DO NOTHING;`
### upsert
  - `INSERT INTO person (id, first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES (4, 'Flo', 'Sexcey', 'fsexcey3@seesaa.com', 'Bigender', '2021-05-22', 'Honduras') ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email;`
### update forign keys columns
  - `UPDATE person SET car_id = 1 WHERE id = 2;`
### inner joins
  - `SELECT * FROM person JOIN car ON person.car_id = car.id;`
  - `SELECT person.first_name, car.maker, car.price FROM person JOIN car ON person.car_id=car.id;`
### left joins
  - `SELECT * FROM person LEFT JOIN car ON person.car_id=car.id;`
  - `SELECT * FROM person LEFT JOIN car ON car.id=person.car_id;`
  - `SELECT * FROM person LEFT JOIN car USING(id);`
  - `SELECT * FROM person LEFT JOIN car ON person.car_id=car.id WHERE car.* is NULL;`
### extract csv
  - `\copy (SELECT * FROM person LEFT JOIN car ON person.car_id=car.id) TO '/postgres/sample_data/result.csv' DELIMITER ',' CSV HEADER;`
### extention
  - `SELECT * FROM pg_available_extension_versions;`
  - `CREATE EXTENSION "uuid-ossp";`
## references
  - https://www.youtube.com/watch?v=qw--VYLpxG4&t=421s
