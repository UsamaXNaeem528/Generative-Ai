select * from marks
select * from students
select * from students_profile

create table courses(
	course_id int serial primary key,
	course_name varchar(100) not null
)

create procedure add_student(s_name varchar(100))
language plpgsql
as $$
Begin 
insert into students(name)
values (s_name);
End;
$$;

call add_student('Harry')

DROP PROCEDURE IF EXISTS add_student(); -- Argument types are often required in PostgreSQL if overloaded procedures exist
