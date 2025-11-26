-- --
-- -- Complete PostgreSQL Script to set up the Employee and Department tables
-- --
-- -- 1. Create DEPARTMENT table
-- -- 2. Create EMPLOYEE table with Foreign Key constraints
-- -- 3. Insert sample data into both tables

-- -- Drop the tables (department first, as employee depends on it)
-- DROP TABLE IF EXISTS employee;
-- DROP TABLE IF EXISTS department CASCADE;


-- -- SECTION 1: DEPARTMENT Table Creation and Data

-- CREATE TABLE department (
--     deptno    INTEGER      PRIMARY KEY,
--     dname     VARCHAR(14)  NOT NULL,
--     loc       VARCHAR(13)
-- );

-- INSERT INTO department (deptno, dname, loc) VALUES
-- (10, 'ACCOUNTING', 'NEW YORK'),
-- (20, 'RESEARCH',   'DALLAS'),
-- (30, 'SALES',      'CHICAGO'),
-- (40, 'OPERATIONS', 'BOSTON');


-- -- SECTION 2: EMPLOYEE Table Creation and Data

-- CREATE TABLE employee (
--     empno      INTEGER      PRIMARY KEY,
--     ename      VARCHAR(10)  NOT NULL,
--     job        VARCHAR(9),
--     mgr        INTEGER,
--     hiredate   DATE         NOT NULL,
--     sal        NUMERIC(7, 2),
--     comm       NUMERIC(7, 2),
--     deptno     INTEGER,
    
--     -- Foreign Key Constraint for DEPTNO linking to the department table
--     CONSTRAINT fk_deptno FOREIGN KEY (deptno) REFERENCES department(deptno),
    
-- );

-- Inserting a general manager (who is their own manager for simplicity, or NULL if allowed)
INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7839, 'KING', 'PRESIDENT', NULL, '1981-11-17', 5000.00, NULL, 10);

-- Inserting managers and other employees in DEPT 10, 20, 30, 40

-- DEPT 10 (Accounting)
INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09', 2450.00, NULL, 10);

INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7934, 'MILLER', 'CLERK', 7782, '1982-01-23', 1300.00, NULL, 10);

-- DEPT 20 (Research)
INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7566, 'JONES', 'MANAGER', 7839, '1981-04-02', 2975.00, NULL, 20);

INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7788, 'SCOTT', 'ANALYST', 7566, '1987-04-19', 3000.00, NULL, 20);

INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7876, 'ADAMS', 'CLERK', 7788, '1987-05-23', 1100.00, NULL, 20);

INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7902, 'FORD', 'ANALYST', 7566, '1981-12-03', 3000.00, NULL, 20);

-- DEPT 30 (Sales)
INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01', 2850.00, NULL, 30);

INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600.00, 300.00, 30);

INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08', 1500.00, 0.00, 30);

INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250.00, 1400.00, 30);

INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7900, 'JAMES', 'CLERK', 7698, '1981-12-03', 950.00, NULL, 30);

-- DEPT 40 (Operations - assumed)
INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (7001, 'SAM', 'OPERATOR', 7839, '2023-01-15', 1800.00, NULL, 40);

-- -- Display the created data
 SELECT * FROM department;
SELECT * FROM employee;

--1
select e.ename, e.sal from employee e where e.sal < (select sal from employee where empno = 7839)


--2
select e.ename, e.sal, (select sal as emp_7839_sal from employee where empno = 7839)
from employee e where e.sal <
	(select sal from employee where empno = 7839)


--3
select e.*, d.dname
from employee e 
join department d 
on e.deptno = d.deptno
where e.deptno = (
	select deptno from employee where empno = 7839
)


--4
select ename, sal, (select round(avg(sal),2) as avg_salary from employee)
from employee where sal >
(select avg(sal) from employee)


--5
select * from employee where hiredate < 
	(select hiredate from employee where ename = upper('blake'))
select * from employee


--6
select ename, sal from employee 
where 
sal > 
(select sal from employee where ename = 'BLAKE')
and 
sal < 
(select sal from employee where ename = 'KING')


--7 
select deptno, count(*) as dept_count from employee 
group by deptno
having count(*) > 
(select count(*) from employee where deptno = 10)


--8
select d.dname 
from department as d
join employee as e
on d.deptno = e.deptno
group by d.dname
having count(*) >
(select count(*) from employee where deptno = 10)


--9
select d.dname 
from department as d
join employee as e
on d.deptno = e.deptno
group by d.dname
having count(*) >
(select count(*) from employee where dname = 10)


--10
select d.dname 
from department as d
join employee as e
on d.deptno = e.deptno
group by d.dname
having count(*) >
(select count(*) from employee where deptno = 
	(select deptno from department where dname =  'ACCOUNTING')
)


--11 Find managers with at least 2 employees reporting to them.
select e.empno, e.ename, e.job from employee as e where e.empno in (
	select m.mgr from employee as m where m.mgr = e.empno
	group by m.mgr
	having count(*) >= 2
)
-- sub query is not efficeint way to solve this question
-- if the table data is large use the joins

SELECT
    m.empno,
    m.ename,
    m.job,
    COUNT(e.empno) AS number_of_reports
FROM
    employee AS e -- e represents the employee being managed (the report)
JOIN
    employee AS m ON e.mgr = m.empno -- m represents the manager
GROUP BY
    m.empno, m.ename, m.job
HAVING
    COUNT(e.empno) >= 2;


select  e.*,( 
			select max(sal) from employee e2
			where e2.deptno = e.deptno)
from employee as e


---Windows Function 
select e.*,max(sal) over(partition by deptno) 
from employee as e


select * from
	(select e.*, rank() over(partition by deptno order by empno) as emp_rank
from employee e)
where emp_rank<=2;

select e.*, dense_rank() over(order by sal desc),
percent_rank() over(order by sal desc) from employee as e


select * from
	  (select e.*, dense_rank() over(partition by deptno order by sal desc) as r
	  from employee as e )
where r<=2

---------------------------------------
----- LAG/LEAD Windows Functions-------
---------------------------------------

--1 display employee detial with ith next employee salary
--2 display employee detial with ith previous employee salary
select e.*, LEAD(sal,1) over(order by empno) from employee e

select e.*, LAG(sal,2,0) over(order by empno) as next_emp_sal from employee e

--2 show High, Lower, Previous with separate column 
-- if salary is higher then previous salary show higher, if lower then show lower, if equal than lower
select sal, prev_emp_sal,
case
	when sal < prev_emp_sal then 'Lower'
	when sal > prev_emp_sal then 'Higher'
	else 'Equal'
End Salary_Badge
from(
select sal, LAG(sal,1,0) over(order by empno) as prev_emp_sal
from employee e
)

--Order Table Query with Lag / Lead

CREATE TABLE ORDER_STATUS_HISTORY (
    ORDER_ID INT NOT NULL,
    STATUS_DATE DATE NOT NULL,
    STATUS VARCHAR(50) NOT NULL
);

INSERT INTO ORDER_STATUS_HISTORY (ORDER_ID, STATUS_DATE, STATUS)
VALUES
    (101, '2025-11-01', 'Order Placed'),
    (101, '2025-11-03', 'Processing'),
    (101, '2025-11-05', 'Shipped'),
    (102, '2025-11-02', 'Order Placed'),
    (102, '2025-11-04', 'Cancelled'),
    (103, '2025-11-01', 'Order Placed'),
    (103, '2025-11-02', 'Processing'),
    (103, '2025-11-06', 'Shipped'),
    (104, '2025-11-03', 'Order Placed'),
    (104, '2025-11-05', 'Processing');

select * from ORDER_STATUS_HISTORY 

-- Question
-- Write a query to produce a table that shows, for each order status:
-- ORDER_ID
-- STATUS
-- The date the order entered this status (from_date)
-- The date the order moved to the next status (to_date)

select order_id, status, 
LAG(status_date ,1) over(partition by order_id order by status_date) as from_date,
LEAD(status_date, 1) over(partition by order_id order by status_date) as to_date 
from ORDER_STATUS_HISTORY
	


WITH latest_status AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY status_date DESC) AS rn
    FROM order_status_history
)
SELECT order_id, status
FROM latest_status
WHERE rn = 1;











 

	
