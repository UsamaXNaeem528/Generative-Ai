create table products(
	product_id serial Primary Key,
	product_name varchar(100) not null,
	category text not null,
	price numeric(10,2) check(price>0),
	stock_quantity int default 0 check (stock_quantity>0),
	is_available boolean default True not null,
	added_on DATE not null
)


create table orders(
	order_id serial Primary Key,
	product_id int not null,
	quantity int check(quantity>0),
	order_date DATE not null,
	customer_name varchar(100) not null,
	payment_method text not null
)

alter table orders
add Constraint  product_id
Foreign Key (product_id)
References products(product_id);



-- Q1. Show each order along with the product name and price.
select 
	p.product_name,
	p.price
	o.order_id,
	o.product_id,
	o.quantity,
	o.order_date, 
	o.customer_name,
	o.payment_method
	from products as p left join orders as o
on p.product_id = o.product_id

select * from products;
select * from orders;

-- Q2. Show all products even if they were never ordered.
select 
	p.product_name,
	p.price,
	o.order_id
from products as p left join orders as o
on p.product_id = o.product_id
where order_id is null;


-- Q3.Show orders for only ‘Electronics’ category
select 
	p.product_name,
	o.order_date,
	o.customer_name
from products as p join orders as o
on p.product_id = o.product_id
where p.category = 'Electronics'


-- Q4.List all orders sorted by product price (high to low)
select
	p.price,
	o.quantity,
	o.order_date,
	o.customer_name
from orders as o join products as p
on o.product_id = p.product_id
order by p.price desc

--Q5.Show number of orders placed for each product
select
	p.product_name,
	count (o.order_id) as no_of_orders
from products as p join orders as o
on p.product_id = o.product_id
group by product_name

--Q6.Show total revenue earned per product
select
	p.product_name,
	sum (p.price * o.quantity) as earned_per_product
from products as p join orders as o
on p.product_id = o.product_id
group by product_name




--  Show products where total order revenue > ₹2000
select
	p.product_name,
	sum(p.price * o.quantity) as earned_per_product
from products as p join orders as o
on p.product_id = o.product_id
group by p.product_name
having sum(p.price * o.quantity) > 2000;

--Show unique customers who ordered ‘Fitness’ products
select
	o.customer_name,
	p.product_name
from products as p join orders as o
on p.product_id = o.product_id
where p.category = 'Fitness'

-- Show the product name and total quantity ordered for each product.
select 
	p.product_name,
	sum(o.quantity) as total_quantity_ordered
from products as p left join orders as o
on p.product_id = o.product_id
group by p.product_name


-- List the top 3 highest earning products based on total revenue (price × quantity).
select * from orders;
select * from products;

select 	
	p.product_name,
	sum(p.price * o.quantity) as total_revenue_per_product
from products as p join orders as o
on p.product_id = o.product_id
group by p.product_name
order by total_revenue_per_product desc
limit 3


-- show all customers with product they purchased
select 
	o.customer_name,
	p.product_name
from orders as o join products as p
on o.product_id = p.product_id











	
	
	


	
	
	















