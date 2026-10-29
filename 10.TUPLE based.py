
# Case Study 10: Tuple-Based Product Catalogue Audit

# Each tuple contains:
# (Product ID, Name, Category, Price, Stock)

products = [
    ("P101", "Keyboard", "Accessories", 750, 12),
    ("P102", "Mouse", "Accessories", 450, 5),
    ("P103", "Monitor", "Electronics", 8500, 3),
    ("P102", "USB Cable", "Accessories", 250, 20),
    ("P104", "Laptop Stand", "Accessories", 1200, 0)
]

total_value = 0
duplicate_ids = []

print("PRODUCT CATALOGUE AUDIT")
print("-" * 60)

# Display product details and perform checks
for product in products:
    product_id, name, category, price, stock = product

    inventory_value = price * stock
    total_value += inventory_value

    print(
        product_id, "|", name, "|", category,
        "| Price: Rs.", price,
        "| Stock:", stock,
        "| Value: Rs.", inventory_value
    )

print("\nLOW-STOCK PRODUCTS (Stock <= 5):")

for product in products:
    product_id, name, category, price, stock = product

    if stock <= 5:
        print(product_id, "-", name, "- Stock:", stock)

print("\nEXPENSIVE PRODUCTS (Price >= Rs. 5000):")

for product in products:
    product_id, name, category, price, stock = product

    if price >= 5000:
        print(product_id, "-", name, "- Price: Rs.", price)

# Find duplicate product IDs
for i in range(len(products)):
    for j in range(i + 1, len(products)):
        if products[i][0] == products[j][0]:
            if products[i][0] not in duplicate_ids:
                duplicate_ids.append(products[i][0])

print("\nDUPLICATE PRODUCT IDs:")

if len(duplicate_ids) > 0:
    for product_id in duplicate_ids:
        print(product_id)
else:
    print("No duplicate IDs found.")

print("\nTOTAL INVENTORY VALUE: Rs.", total_value)
print("AUDIT COMPLETED")
