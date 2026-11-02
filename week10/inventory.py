# Module 10 Lab - Inventory List Manager
# Name: Yashvini Jamnadas
# ISM2411 - Fall 2026
#
# Reflection
# 1. The most surprising thing about Python lists is how much you can do with
#    one line, like grabbing every other item with [::2] or the last items with
#    negative indexes. I also didn't expect a list to start counting at 0, so
#    the "first" item is really position 0.
#
# 2. For my business, LYK Studios, I track local businesses I've reached out to.
#    Keeping their names or follower counts in a Python list would let me sort,
#    filter, and average them instantly instead of re-sorting and writing
#    formulas in Excel every time I add someone new.


# Exercise 1
print("--- Exercise 1: Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# Exercise 2
print("\n--- Exercise 2: Index practice ---")
print(inventory[0])                    # first item
print(inventory[-1])                   # last item
middle = len(inventory) // 2
print(inventory[middle])               # middle item


# Exercise 3
print("\n--- Exercise 3: Slicing ---")
print(inventory[:3])                   # first three
print(inventory[-2:])                  # last two
print(inventory[::2])                  # every other item


# Exercise 4
print("\n--- Exercise 4: Modify ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)


# Exercise 5
print("\n--- Exercise 5: Tuple comparison ---")
coords = (40.7128, -74.0060)           # NYC latitude, longitude
try:
    coords[0] = 99
except TypeError as error:
    print("Error caught:", error)
    print("Tuples can't be changed, which is good for coordinates because "
          "a location's latitude and longitude should stay fixed.")
print(coords)


# Exercise 6
print("\n--- Exercise 6: Sales statistics ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best day:", max(sales))
print("Worst day:", min(sales))


# Exercise 7
print("\n--- Exercise 7: Accumulator ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print("Original:", prices)
print("Discounted:", discounted)


# Exercise 8
print("\n--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))
