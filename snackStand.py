name = input("What's your first name? ").strip().capitalize()
snack = input("What are you buying? ").strip().title()
price = float(input("Price of snack: "))
quantity = int(input("Quantity of snack: "))
subtotal = price * quantity

if subtotal >= 10:
    discount = subtotal % 10
else:
    discount = 0

print("")
print("####OUTPUT####")
print(f"Customer: {name}")
print(f"Snack: {snack}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal}")
print(f"Discount: ${discount}")
print(f"Final total: ${subtotal - discount}")