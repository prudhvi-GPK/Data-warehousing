-- Insert sample customers
INSERT INTO customers (name, email) VALUES
('John Doe', 'john@example.com'),
('Jane Smith', 'jane@example.com'),
('Bob Johnson', 'bob@example.com'),
('Alice Brown', 'alice@example.com'),
('Charlie Davis', 'charlie@example.com');

-- Insert sample products
INSERT INTO products (name, price, stock_quantity) VALUES
('Laptop', 999.99, 50),
('Smartphone', 599.99, 100),
('Headphones', 99.99, 200),
('Tablet', 299.99, 75),
('Smartwatch', 199.99, 150);

-- Insert sample orders
INSERT INTO orders (customer_id, total_amount) VALUES
(1, 1099.98),
(2, 699.98),
(3, 399.98),
(4, 299.99),
(5, 1299.97);

-- Insert sample order items
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 999.99),
(1, 3, 1, 99.99),
(2, 2, 1, 599.99),
(2, 3, 1, 99.99),
(3, 4, 1, 299.99),
(3, 3, 1, 99.99),
(4, 4, 1, 299.99),
(5, 1, 1, 999.99),
(5, 2, 1, 599.99);