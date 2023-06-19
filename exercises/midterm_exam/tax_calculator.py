def estimate_tax_increase_travelled(travelled, target_km, target_euro):
    tax_increase_travelled = travelled // target_km
    return tax_increase_travelled * target_euro


def estimate_tax_increase_years(initial_tax_value, years, target_euro):
    tax_increase_years = initial_tax_value - years * target_euro
    return tax_increase_years


vehicles_to_be_taxed = input()
vehicle_details = vehicles_to_be_taxed.split(">>")
vehicle_breakdown = [i.split() for i in vehicle_details]


total_taxed = []

for instance in vehicle_breakdown:
    tax_total_increase = 0
    car_type, tax_years, kilometers_travelled = instance[0], int(instance[1]), int(instance[2])
    if car_type == "family":
        initial_tax = 50
        target_euro_travelled = 12
        target_euro_years = 5
        target_kilometers = 3000
        tax_travelled_increase = estimate_tax_increase_travelled(kilometers_travelled,
                                                                 target_kilometers, target_euro_travelled)
        tax_years_increase = estimate_tax_increase_years(initial_tax, tax_years, target_euro_years)
        tax_total_increase = tax_travelled_increase + tax_years_increase
        total_taxed.append(tax_total_increase)
        print(f"A {car_type} car will pay {tax_total_increase:.2f} euros in taxes.")
    elif car_type == "heavyDuty":
        initial_tax = 80
        target_euro_travelled = 14
        target_euro_years = 8
        target_kilometers = 9000
        tax_travelled_increase = estimate_tax_increase_travelled(kilometers_travelled, target_kilometers,
                                                                 target_euro_travelled)
        tax_years_increase = estimate_tax_increase_years(initial_tax, tax_years, target_euro_years)
        tax_total_increase = tax_travelled_increase + tax_years_increase
        total_taxed.append(tax_total_increase)
        print(f"A {car_type} car will pay {tax_total_increase:.2f} euros in taxes.")
    elif car_type == "sports":
        initial_tax = 100
        target_euro_travelled = 18
        target_euro_years = 9
        target_kilometers = 2000
        tax_travelled_increase = estimate_tax_increase_travelled(kilometers_travelled, target_kilometers,
                                                                 target_euro_travelled)
        tax_years_increase = estimate_tax_increase_years(initial_tax, tax_years, target_euro_years)
        tax_total_increase = tax_travelled_increase + tax_years_increase
        total_taxed.append(tax_total_increase)
        print(f"A {car_type} car will pay {tax_total_increase:.2f} euros in taxes.")
    elif car_type not in ["family", "heavyDuty", "sports"]:
        print("Invalid car type.")

sum_tax = sum(total_taxed)
print(f"The National Revenue Agency will collect {sum_tax:.2f} euros in taxes.")
