
# Product Pricing and Profit Calculator

# Ask for the product name and store it in product_name
product_name = input("Enter the product name: ").strip().title()


# Ask for the quantity, convert it to an integer, and store it in quantity
quantity = int(input("Enter the quantity: "))


# Ask for the purchase price per unit in KES, convert it to a float,
# and store it in unit_purchase_price.
unit_purchase_price = float(input("Enter the purchase price per unit in KES: "))


# Ask for the selling price per unit in KES, convert it to a float,
# and store it in unit_selling_price.
unit_selling_price = float(input("Enter the selling price per unit in KES: "))

# Display the product name with a clear label.
print(f"Product Name: {product_name}")


# Display the quantity with a clear label.
print(f"Quantity: {quantity}")


# Display the purchase price per unit with a clear label and KES.
print(f"Purchase Price per Unit: KES {unit_purchase_price:.2f}")


# Display the selling price per unit with a clear label and KES.
print(f"Selling Price per Unit: KES {unit_selling_price:.2f}")