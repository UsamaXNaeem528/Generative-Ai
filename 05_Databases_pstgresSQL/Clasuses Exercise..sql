----------------------------------------------
-----------------CLAUSES TEST-----------------
----------------------------------------------

-- 1
select name, price from product;

-- 2
select * from product where category = 'Electronics'

--3
select category from product group by category;

--4
select category, count(*) from product
group by category
having count(*) > 2

--5
select * from product
order by price asc

--6 
select * from product limit(3)

--7
select name as Item_name, price as Item_Price from product;

--8
select DISTINCT(category) from product; 


----------------------------------------------
-----------------TEST 2-----------------------
----------------------------------------------

select * from product;

--1
select name, price from product
order by price asc
limit 1;
--OR
select name, price from product where price = (select min(price) from product);

--2 Find the average price of products that belong to the 'Home & Office' or 'Fitness' category.
select  name, category, round(avg(price),2) as Avg_Price from product where category = 'Home & Office' or category = 'Electronics'
group by name, category;


--3 Show product names and stock quantity where the product is available, stock is more than 50, and price is not equal to ₹299.
select name, stock_quantity from product 
where is_available = true
and stock_quantity > 50 
and price != 299

--4 Find the most expensive product in each category (name and prices)
select name, price from product where price = (select max(price) from product)

--5  Show all unique categories in uppercase, sorted in descending order
select distinct upper(category) as category_upper  from product 
order by category_upper asc;








