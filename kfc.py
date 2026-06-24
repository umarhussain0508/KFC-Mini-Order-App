kfc_items = ["Chicken", "Burger", "Fries", "Coleslaw", "Mashed Potatoes",
             "Gravy", "Biscuits", "Soft Drinks", "Desserts"]

kfc_prices = [5.99, 4.99, 2.99, 3.49, 3.99,
              1.99, 1.49, 1.99, 2.49]

# Take multiple items
order = input("Enter items separated by commas: ")

# Convert input into a list
ordered_items = [item.strip() for item in order.split(",")]

total = 0
valid_items = []

print("\n--- Order Details ---")

for item in ordered_items:
    if item in kfc_items:
        index = kfc_items.index(item)
        price = kfc_prices[index]

        valid_items.append(item)
        total += price

        print(f"{item}: ${price:.2f}")
    else:
        print(f"Sorry, {item} is not available on the menu.")

confirm = input("\nDo you want to confirm your order? (yes/no): ")
dine_or_takeaway = input("Is this order for dine-in or takeaway? (dine-in/takeaway): ")

if confirm.lower() == "yes":
    print("\n---- BILL ----")

    for item in valid_items:
        index = kfc_items.index(item)
        print(f"{item}: ${kfc_prices[index]:.2f}")

    print(f"Order Type: {dine_or_takeaway}")
    print(f"Total: ${total:.2f}")
    print("Thank you for your order!")
else:
    print("Order cancelled.")
