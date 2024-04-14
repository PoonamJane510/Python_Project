# Python_Project
For testflask.py
Prerequisites :
Python
flask
SQL lite

Steps to follow
-- Create the products table
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
);

-- Insert example data into the products table
INSERT INTO products (name, price) VALUES ('Product 1', 10.99);
INSERT INTO products (name, price) VALUES ('Product 2', 20.49);
INSERT INTO products (name, price) VALUES ('Product 3', 15.99);

Run the flasktest.py file
open url in the browser 'http://127.0.0.1:5000/products'
All the products in the data base will be visible
