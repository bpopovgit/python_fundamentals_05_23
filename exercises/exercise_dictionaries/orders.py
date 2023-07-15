products = {}
while True:
    product_info = input().split()
    if product_info[0] == "buy":
        break
    product_name, product_price, product_quantity = product_info[0], float(product_info[1]), int(product_info[2])
    if product_name not in products.keys():
        products[product_name] = [product_price, product_quantity]
    else:
        products[product_name][0] = product_price
        products[product_name][1] += product_quantity

for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")