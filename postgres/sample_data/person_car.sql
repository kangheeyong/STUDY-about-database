create table car (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	maker VARCHAR(100) NOT NULL,
	model VARCHAR(100) NOT NULL,
	price NUMERIC(19, 2) NOT NULL
);

create table person (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(150),
	gender VARCHAR(50) NOT NULL,
	date_of_birth DATE NOT NULL,
	country_of_birth VARCHAR(50),
    car_id BIGINT REFERENCES car (id),
    UNIQUE(car_id)
);


insert into person (first_name, last_name, email, gender, date_of_birth, country_of_birth) values ('Sandye', 'Flag', 'sflag0@globo.com', 'Female', '2020-07-24', 'Indonesia');
insert into person (first_name, last_name, email, gender, date_of_birth, country_of_birth) values ('Carolan', 'Hitzschke', 'chitzschke1@studiopress.com', 'Agender', '2021-07-04', 'Albania');
insert into person (first_name, last_name, email, gender, date_of_birth, country_of_birth) values ('Nicolis', 'Hinder', 'nhinder2@furl.net', 'Non-binary', '2020-10-12', 'Thailand');

insert into car (maker, model, price) values ('Mercedes-Benz', 'C-Class', 30075);
insert into car (maker, model, price) values ('Ford', 'Freestar', 44977);
insert into car (maker, model, price) values ('Maserati', 'Gran Sport', 16716);


