select * from products

--Indexing creates a lookup table (virually) with the column and the pointer to the memory location of the row, containing this column.
-- - If rows increase from 100 to 1million in table, how will you optimise it? Using indexing.
-- - Previously was taking O(n), now it will take O(logn), as mainly we are using Binary search Tree for indexing.
-- - It is mainly used for read intensive application, not for write intensive application.

create index idx_product_name
on products(product_name)

SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'products';

drop index idx_product_name
select * from products where product_name = 'Wireless Charger'

-- Primary key table → index already exists

-- Foreign key table → you must create an index

-- JOIN works fastest when both sides of the JOIN condition are indexed.

