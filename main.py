from database import *

# creare tabele
create_tables()

# produse
products_data = [
    ("Laptop", "Electronics"),
    ("Telefon", "Electronics"),
    ("Mouse", "Accessories")
]

insert_products(products_data)

# vânzări (product_id, quantity, price)
sales_data = [
    (1, 2, 3500),
    (2, 5, 2000),
    (3, 10, 150),
    (1, 1, 3500),
    (2, 2, 2000)
]

insert_sales(sales_data)

print("=== RAPORT VÂNZĂRI ===")
for row in get_sales_report():
    print(row)

print("\n=== DOAR ELECTRONICS ===")
for row in get_sales_by_category("Electronics"):
    print(row)


print("\n=== DOAR ACCESORIES ===")
for row in get_sales_by_category("Accessories"):
    print(row)
