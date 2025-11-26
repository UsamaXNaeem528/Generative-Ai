create table employee(
	employee_id serial Primary Key,
	employee_name varchar(100) not null,
	department varchar(100) not null,
	hire_date Date not null
)

create table project(
	project_id serial Primary Key,
	project_name varchar(100) not null,
	project_budget numeric(10,2) check (project_budget>0),
	start_date Date not null
)

create table Employee_Projects(
	assign_date Date not null,
	role_in_project varchar not null,
	employee_id int not null,
	project_id int not null,
	 Primary Key(employee_id, project_id),
	Foreign Key (employee_id) references employee(employee_id),
	Foreign Key (project_id) references project(project_id)
)

insert into employee (employee_name, department, hire_date) values
('Ali Raza', 'IT', '2023-02-15'),
('Sara Khan', 'Marketing', '2022-10-01'),
('John Smith', 'Finance', '2024-01-12'),
('Ayesha Noor', 'IT', '2023-08-20');

insert into project (project_name, project_budget, start_date) values
('Website Redesign', 250000.00, '2024-03-01'),
('Digital Marketing Campaign', 150000.00, '2024-01-20'),
('Financial Audit System', 300000.00, '2024-02-10'),
('Mobile App Development', 500000.00, '2024-04-05');




insert into employee_projects (assign_date, role_in_project, employee_id, project_id) values
('2024-03-05', 'Backend Developer', 1, 1),   -- Ali on Website Redesign
('2024-04-10', 'Lead Developer', 1, 4),      -- Ali on Mobile App Dev

('2024-01-25', 'Campaign Manager', 2, 2),    -- Sara on Marketing Campaign
('2024-04-15', 'Content Strategist', 2, 1),  -- Sara also works on Website Redesign

('2024-02-15', 'Financial Analyst', 3, 3),   -- John on Financial Audit System

('2024-04-12', 'UI/UX Designer', 4, 4),      -- Ayesha on Mobile App Development
('2024-03-08', 'Frontend Developer', 4, 1);  -- Ayesha on Website Redesign

insert into project (project_name, project_budget, start_date) values
('Ai Chatbot', 30000.00, '2024-09-10')
insert into employee_projects (assign_date, role_in_project, employee_id, project_id) values
('2024-11-10', 'Full Stack', 1, 5)

select * from project


select 
	e.employee_name,
	p.project_name,
	ep.role_in_project
from employee as e join employee_projects as ep on e.employee_id = ep.employee_id
join project as p on p.project_id = ep.project_id 



-- Show project details with total number of employees in each project.
select 
	p.project_name,
	count(ep.employee_id) as no_of_employees_per_project
from project as p
join employee_projects as ep on p.project_id = ep.project_id
group by p.project_name


-- Q4) Show employee name and number of projects they are working on.
select 
	e.employee_name,
	count(ep.project_id) as per_emp_work_project
from employee as e
join employee_projects as ep on e.employee_id = ep.employee_id
group by e.employee_name
	
--show employee details and list ALL projects they work on in one row.
select
    e.employee_name,
    string_agg(p.project_name, ', ') as projects
from employee e
join employee_projects ep on e.employee_id = ep.employee_id
join project p on ep.project_id = p.project_id
group by e.employee_name;


-- Show which department is handling the most projects.
select
    e.department,
    count(distinct ep.project_id) as total_projects
from employee e
join employee_projects ep on e.employee_id = ep.employee_id
group by e.department
order by total_projects desc;


