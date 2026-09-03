create database elt_dbs4;

use elt_dbs4;


CREATE TABLE users (
    id INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    age INT,
    gender VARCHAR(20),
    email VARCHAR(150),
    phone VARCHAR(50),
    birthDate DATE,
    role VARCHAR(20),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    postalCode VARCHAR(20)
);

select * from users

select 
firstName + ' ' + lastName as fullname,
email,gender,age
from users
where age > 33

select 
firstName + ' ' + lastName as fullname,
email,gender,age
from users
where email like '%Dummyjson.com'

select 
firstName + ' ' + lastName as fullname,
email,gender,age
from users
where age between 30 and 40
