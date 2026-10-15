
stock = {
    "W001": ("Rolex Submariner", 1500),
    "W002": ("Casio G-Shock", 120),
    "S001": ("Nike Air Max", 90),
    "S002": ("Adidas Yeezy", 200),
    "S003": ("Rolex Submariner", 1500)
}

daily_orders = ["W001", "S001", "W001", "S002", "S001", "S001", "W002"]

# QUESTION 1: Unpack the tuple for S002
name, price = stock["S002"]
print(f"{name} costs ${price}")

# Error when trying to change a tuple
# stock["W001"][0] = "Rolex Daytona"
# TypeError: 'tuple' object does not support item assignment


# QUESTION 2 (i): Find unique products ordered
unique_products = set(daily_orders)
print("\nUnique products ordered:", unique_products)

# QUESTION 2 (ii): Find products never ordered
all_products = set(stock.keys())
ordered_products = set(daily_orders)
not_ordered = all_products - ordered_products
print("Products not ordered:", not_ordered)


# QUESTION 3 (i): Add a new product
stock["S004"] = ("Puma RS", 110)
print("\nUpdated stock:", stock)


# QUESTION 3 (ii): Count orders for each product ID
order_count = {}

for product_id in daily_orders:
    order_count[product_id] = order_count.get(product_id, 0) + 1

print("\nOrder count:", order_count)


# QUESTION 3 (iii): Calculate total sales for the day
total_sales = 0

for product_id, quantity in order_count.items():
    price = stock[product_id][1]
    total_sales += price * quantity

print("Total sales for the day: $", total_sales)
