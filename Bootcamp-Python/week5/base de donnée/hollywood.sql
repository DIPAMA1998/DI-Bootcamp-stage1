-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";
	
	create table actors (
	actor_id serial primary key,
	first_name varchar (50) not null,
	last_name varchar (100) not null,
	age date not null,
	number_oscars smallint not null)