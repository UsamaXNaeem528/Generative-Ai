-- create table product(
-- 	Product_ID serial Primary Key,
-- 	name varchar(100) Not null,
-- 	sku_code char(8) unique not null check (char_length(sku_code) = 8),
-- 	Price numeric(10,2) Check(Price>0),
-- 	Stock_Quantity int default 0 Check(Stock_Quantity>0),
-- 	is_available boolean DEFAULT TRUE,
-- 	Category text not null,
-- 	Added_on Date default Current_Date,
-- 	last_updated TIMESTAMP default now()
-- )

-- select * from product;

INSERT INTO product (name, sku_code, price, stock_quantity, is_available, category)
VALUES 
('Wireless Mouse', 'SKU10001', 19.99, 50, TRUE, 'Electronics'),
('Gaming Keyboard', 'SKU10002', 69.99, 30, TRUE, 'Electronics'),
('Office Chair', 'SKU10003', 149.50, 20, TRUE, 'Furniture'),
('LED Desk Lamp', 'SKU10004', 29.99, 40, TRUE, 'Home & Office'),
('USB-C Cable', 'SKU10005', 9.49, 100, TRUE, 'Accessories');


-- INSERT INTO product (name, sku_code, price, stock_quantity, is_available, category)
-- VALUES 
-- ('Portable Power Bank', 'SKU10000', 39.99, 60, TRUE, 'Electronics');


select * from product;



