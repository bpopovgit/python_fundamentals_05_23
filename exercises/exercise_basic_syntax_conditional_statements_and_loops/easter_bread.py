budget = float(input())
price_for_one_kg_flour = float(input())
price_for_one_pack_of_eggs = price_for_one_kg_flour * 0.75
price_for_one_liter_milk = price_for_one_kg_flour + price_for_one_kg_flour * 0.25
price_for_needed_milk = price_for_one_liter_milk / 4

price_for_one_loaf = price_for_one_kg_flour + price_for_one_pack_of_eggs + price_for_needed_milk

num_of_loaves_made = 0
colored_eggs = 0

while budget >= price_for_one_loaf:
    num_of_loaves_made += 1
    budget -= price_for_one_loaf
    colored_eggs += 3
    if num_of_loaves_made % 3 == 0:
        colored_eggs -= (num_of_loaves_made - 2)

print(f"You made {num_of_loaves_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")



