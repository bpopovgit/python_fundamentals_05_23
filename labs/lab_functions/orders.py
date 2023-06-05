def calculate_orders(product_one, quantity_one):
    result = ""
    if product == "coffee":
        result = quantity * 1.50
    elif product == "coke":
        result = quantity * 1.40
    elif product == "water":
        result = quantity * 1.00
    elif product == "snacks":
        result = quantity * 2.00
    return f"{result:.2f}"


product = input()
quantity = float(input())
print(calculate_orders(product, quantity))
