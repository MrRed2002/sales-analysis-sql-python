import sqlite3

def create_connection():
    return sqlite3.connect("sales.db")

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # tabel produse
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT
    )
    """)

    # tabel vânzări
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity INTEGER,
        price REAL,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    """)

    conn.commit()
    conn.close()


def insert_products(data):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO products (name, category) VALUES (?, ?)",
        data
    )

    conn.commit()
    conn.close()


def insert_sales(data):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO sales (product_id, quantity, price) VALUES (?, ?, ?)",
        data
    )

    conn.commit()
    conn.close()


def get_sales_report():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.name, p.category, SUM(s.quantity) as total_quantity,
           SUM(s.quantity * s.price) as total_revenue
    FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY p.name, p.category
    ORDER BY total_revenue DESC
    """)

    results = cursor.fetchall()
    conn.close()
    return results


def update_price(product_id, new_price):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE sales
    SET price = ?
    WHERE product_id = ?
    """, (new_price, product_id))

    conn.commit()
    conn.close()


def delete_sales(product_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM sales
    WHERE product_id = ?
    """, (product_id,))

    conn.commit()
    conn.close()

def get_sales_by_category(category):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.name, SUM(s.quantity) as total_quantity,
           SUM(s.quantity * s.price) as total_revenue
    FROM sales s
    JOIN products p ON s.product_id = p.id
    WHERE p.category = ?
    GROUP BY p.name
    ORDER BY total_revenue DESC
    """, (category,))

    results = cursor.fetchall()
    conn.close()
    return results
