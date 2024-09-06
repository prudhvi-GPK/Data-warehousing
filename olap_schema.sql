\c olap_db

-- Create dimension tables
CREATE TABLE dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_id INTEGER,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at DATE
);

CREATE TABLE dim_product (
    product_key SERIAL PRIMARY KEY,
    product_id INTEGER,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE dim_date (
    date_key SERIAL PRIMARY KEY,
    date DATE,
    day INTEGER,
    month INTEGER,
    year INTEGER,
    quarter INTEGER
);

-- Create fact table
CREATE TABLE fact_sales (
    sales_key SERIAL PRIMARY KEY,
    order_id INTEGER,
    customer_key INTEGER REFERENCES dim_customer(customer_key),
    product_key INTEGER REFERENCES dim_product(product_key),
    date_key INTEGER REFERENCES dim_date(date_key),
    quantity INTEGER,
    total_amount DECIMAL(10, 2)
);

-- Create indexes for better OLAP performance
CREATE INDEX idx_fact_sales_customer ON fact_sales(customer_key);
CREATE INDEX idx_fact_sales_product ON fact_sales(product_key);
CREATE INDEX idx_fact_sales_date ON fact_sales(date_key);