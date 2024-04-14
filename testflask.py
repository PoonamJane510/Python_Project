from flask import Flask, jsonify, request, abort
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect("sqlite.db")
conn.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price REAL
                )''')
conn.close()

# GET /products - Retrieve a list of all products
@app.route('/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return jsonify(products)

# GET /products/{id} - Retrieve details of a specific product by its ID
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (id,))
    product = cursor.fetchone()
    conn.close()
    if product:
        return jsonify(product)
    else:
        abort(404)

# POST /products - Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        abort(400)
    new_product = (request.json['name'], request.json['price'])
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", new_product)
    conn.commit()
    new_product_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": new_product_id, "name": request.json['name'], "price": request.json['price']}), 201

# PUT /products/{id} - Update an existing product based on its ID
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (id,))
    product = cursor.fetchone()
    if not product:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) not in [float, int]:
        abort(400)
    updated_product = {
        'name': request.json.get('name', product[1]),
        'price': request.json.get('price', product[2])
    }
    cursor.execute("UPDATE products SET name=?, price=? WHERE id=?", (updated_product['name'], updated_product['price'], id))
    conn.commit()
    cursor.execute("SELECT * FROM products WHERE id=?", (id,))
    updated_product = cursor.fetchone()
    conn.close()
    return jsonify(updated_product)

# DELETE /products/{id} - Delete a product by its ID
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (id,))
    product = cursor.fetchone()
    if not product:
        abort(404)
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'result': True})


if __name__ == '__main__':
    # Insert sample data
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Product 1", 10.99))
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Product 2", 20.49))
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Product 3", 15.99))
    conn.commit()
    conn.close()

    # Run the Flask app
    app.run(debug=True)
