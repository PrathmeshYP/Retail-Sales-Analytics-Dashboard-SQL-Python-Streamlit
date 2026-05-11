DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    product TEXT,
    category TEXT,
    quantity INT,
    price REAL,
    region TEXT
);