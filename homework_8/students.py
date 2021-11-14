create table students (
	id INT Primary key,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	group_id int,
	FOREIGN KEY (group_id) REFERENCES groups (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

insert into students (id, first_name, last_name, group_id) values (1, 'Garald', 'Ballister', 3);
insert into students (id, first_name, last_name, group_id) values (2, 'Jammie', 'Gladhill', 1);
insert into students (id, first_name, last_name, group_id) values (3, 'Cosme', 'Sharratt', 2);
insert into students (id, first_name, last_name, group_id) values (4, 'Rolf', 'Challenor', 1);
insert into students (id, first_name, last_name, group_id) values (5, 'Marylou', 'Dewick', 1);
insert into students (id, first_name, last_name, group_id) values (6, 'Angelina', 'Gyorgy', 1);
insert into students (id, first_name, last_name, group_id) values (7, 'Veradis', 'McCartney', 3);
insert into students (id, first_name, last_name, group_id) values (8, 'Ardis', 'Dare', 1);
insert into students (id, first_name, last_name, group_id) values (9, 'Angelia', 'Sweating', 2);
insert into students (id, first_name, last_name, group_id) values (10, 'Godard', 'Poli', 1);
insert into students (id, first_name, last_name, group_id) values (11, 'Larisa', 'Cockman', 1);
insert into students (id, first_name, last_name, group_id) values (12, 'Lori', 'Lymer', 1);
insert into students (id, first_name, last_name, group_id) values (13, 'Nevile', 'Etherson', 2);
insert into students (id, first_name, last_name, group_id) values (14, 'Ric', 'Craighead', 3);
insert into students (id, first_name, last_name, group_id) values (15, 'Hadlee', 'Tew', 2);
insert into students (id, first_name, last_name, group_id) values (16, 'Lynsey', 'Rishman', 2);
insert into students (id, first_name, last_name, group_id) values (17, 'Nils', 'Lucchi', 3);
insert into students (id, first_name, last_name, group_id) values (18, 'Jorge', 'Watters', 1);
insert into students (id, first_name, last_name, group_id) values (19, 'Stephanie', 'Escudier', 2);
insert into students (id, first_name, last_name, group_id) values (20, 'Rudolfo', 'Lockitt', 3);
insert into students (id, first_name, last_name, group_id) values (21, 'Manolo', 'Hakking', 2);
insert into students (id, first_name, last_name, group_id) values (22, 'Harland', 'Jouhandeau', 1);
insert into students (id, first_name, last_name, group_id) values (23, 'Ulberto', 'Traice', 3);
insert into students (id, first_name, last_name, group_id) values (24, 'Eadie', 'Hatry', 1);
insert into students (id, first_name, last_name, group_id) values (25, 'Trev', 'Edghinn', 3);
insert into students (id, first_name, last_name, group_id) values (26, 'Julietta', 'Soar', 2);
insert into students (id, first_name, last_name, group_id) values (27, 'Meir', 'Kohter', 3);
insert into students (id, first_name, last_name, group_id) values (28, 'Jessalin', 'Meuse', 1);
insert into students (id, first_name, last_name, group_id) values (29, 'Hubey', 'Feilden', 1);
insert into students (id, first_name, last_name, group_id) values (30, 'Portie', 'Whyffen', 1);