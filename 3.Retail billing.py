
# Retail Billing with Multiple Discount Rules

products = []

number_of_products = int(input("Enter number of products: "))

if number_of_products <= 0:
    print("Please enter a valid number of products.")

else:
    valid_categories = ["electronics", "clothing", "grocery"]

    for i in range(number_of_products):
        print("\nProduct", i + 1)

        name = input("Enter product name: ").strip()
        category = input(
            "Enter category (electronics/clothing/grocery): "
        ).strip().lower()
        price = float(input("Enter price: Rs. "))
        quantity = int(input("Enter quantity: "))

        if (not name or category not in valid_categories
                or price < 0 or quantity <= 0):
            print("Invalid product details. Please run again.")
            break

        product_total = price * quantity

        products.append({
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "total": product_total
        })

    else:
        subtotal = sum(product["total"] for product in products)

        # Calculate discount
        if subtotal >= 2000:
            discount = min(subtotal * 0.10, 500)
        else:
            discount = 0

        total_tax = 0

        print("\n========== RETAIL INVOICE ==========")
        print("Product       Qty    Amount")
        print("------------------------------------")

        for product in products:
            if subtotal > 0:
                share = product["total"] / subtotal
                allocated_discount = discount * share
            else:
                allocated_discount = 0

            taxable_amount = product["total"] - allocated_discount

            if product["category"] == "electronics":
                tax_rate = 0.18
            elif product["category"] == "clothing":
                tax_rate = 0.05
            else:
                tax_rate = 0.00

            tax = taxable_amount * tax_rate
            total_tax += tax

            print(
                product["name"],
                product["quantity"],
                "Rs.", round(product["total"], 2)
            )

        final_bill = subtotal - discount + total_tax

        print("------------------------------------")
        print("Subtotal       : Rs.", round(subtotal, 2))
        print("Discount       : Rs.", round(discount, 2))
        print("Total Tax      : Rs.", round(total_tax, 2))
        print("Final Bill     : Rs.", round(final_bill, 2))
        print("====================================")
