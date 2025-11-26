-- create table students(
-- 	student_id serial Primary Key,
-- 	name varchar(100)
-- )

-- INSERT INTO students (name)
-- VALUES
-- ('Ali Raza'),
-- ('Sara Khan'),
-- ('John Smith');

-- select * from students;

-- create table students_profile(
-- 	student_id int Primary Key,
-- 	address varchar(100),
-- 	age int,
-- 	phone varchar(100)
-- )

-- INSERT INTO students_profile (student_id, address, age, phone)
-- VALUES
-- (1, 'Lahore, Pakistan', 20, '0300-1234567'),
-- (2, 'Karachi, Pakistan', 22, '0311-7654321'),
-- (3, 'Islamabad, Pakistan', 19, '0322-9876543');


-- select * from students_profile;

-- alter table students_profile
-- add constraint fk_student_id
-- Foreign Key (student_id)
-- References students(student_id); 

-- select * from students_profile;


-- select 
-- 	s.student_id,
-- 	s.name,
-- 	sp.address,
-- 	sp.age,
-- 	sp.phone
-- from students s
-- join students_profile sp
-- on s.student_id = sp.student_id;


-- create table students(
-- 	student_id serial Primary Key,
-- 	name varchar(100)
-- )

-- create table marks(
-- 	marks_id serial Primary Key,
-- 	student_id int,
-- 	subject_name varchar(100),
-- 	marks int,
-- 	Foreign Key(student_id) References students(student_id)
-- )


-- INSERT INTO marks (student_id, subject_name, marks)
-- VALUES
-- -- Ali Raza
-- (1, 'Math', 85),
-- (1, 'English', 78),
-- (1, 'Science', 92),

-- -- Sara Khan
-- (2, 'Math', 88),
-- (2, 'English', 81),
-- (2, 'Science', 89),

-- -- John Smith
-- (3, 'Math', 75),
-- (3, 'English', 80),
-- (3, 'Science', 70);

-- select * from students
-- select * from marks;

-- --1
-- select 
-- 	s.name,
-- 	m.subject_name,
-- 	m.marks
-- from students as s join marks as m
-- on s.student_id = m.student_id;

-- --2
-- select 
-- 	s.name,
-- 	m.subject_name,
-- 	m.marks
-- from students as s join marks as m
-- on s.student_id = m.student_id 
-- where name = 'Ali Raza';


-- --3
-- select 
-- 	s.name,
-- 	m.subject_name,
-- 	m.marks
-- from students as s join marks as m
-- on s.student_id = m.student_id 
-- where marks>80;

-- --4 
-- select 
-- 	s.name,
-- 	m.subject_name,
-- 	m.marks
-- from students as s join marks as m
-- on s.student_id = m.student_id 
-- order by m.marks desc

-- --5
-- select 
-- 	s.name,
-- 	round(avg(m.marks),2)
-- from students as s join marks as m
-- on s.student_id = m.student_id 
-- group by s.name











	
