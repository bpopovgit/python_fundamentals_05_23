def get_regular_summary(total_price_without_taxes_in, total_tax_price, total_price_with_taxes):
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes:"
          f" {total_price_without_taxes_in:.2f}$\n"
          f"Taxes: {total_tax_price:.2f}$\n-----------\nTotal price: {total_price_with_taxes:.2f}$")


def get_special_summary(total_price_without_taxes_in, total_tax_price, total_price_with_taxes):
    discount = total_price_with_taxes * 0.10
    total_price_with_taxes -= discount
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes:"
          f" {total_price_without_taxes_in:.2f}$\n"
          f"Taxes: {total_tax_price:.2f}$\n-----------\nTotal price: {total_price_with_taxes:.2f}$")


def estimate_output(price_total_without_taxes):
    total_tax_price = price_total_without_taxes * 0.20
    total_price_with_taxes = price_total_without_taxes + total_tax_price

    if customer == "regular":
        if price_total_without_taxes == 0:
            print("Invalid order!")
        else:
            get_regular_summary(price_total_without_taxes, total_tax_price, total_price_with_taxes)

    elif customer == "special":
        if price_total_without_taxes == 0:
            print("Invalid order!")
        else:
            get_special_summary(price_total_without_taxes, total_tax_price, total_price_with_taxes)


total_price_without_taxes = 0
customer = ""

while True:
    command = input()
    customer = command
    if customer == "special" or customer == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        continue
    total_price_without_taxes += price
    if total_price_without_taxes == 0:
        print("Invalid order!")
        break

estimate_output(total_price_without_taxes)
