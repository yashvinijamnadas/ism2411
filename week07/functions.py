#
# ISM2411 Module 7 Lab: Functions + Debug First, Then Ask
#
# Self-Assessment Answers
#
# Q1 :
# The first one I caught was the missing colon on "for sale in sales".
# Python threw a SyntaxError and pointed right at that line, so I didn't
# even need a print() statement to find it. The traceback handed it to me.
# The other two took more digging. One was total getting overwritten
# instead of added up, and the other was the while loop running one index
# too far. My traceback reading is decent, but my eye for logic bugs that
# don't crash the program is still pretty weak.
#
# Q2 :
# You give it a price and a membership tier as a word. It takes a
# percentage off the price depending on the tier. Gold saves the most,
# bronze the least, and anything it doesn't recognize pays full price.
# Then it gives you back the new price. A coworker could call it just from
# the name. They would never need to read the if/elif inside.
#
# Q3 (AI disclosure):
# I used Claude as an explainer in Exercise 5. I pasted in only the error
# text and asked what it meant. I did not ask for the fix. Then I wrote and
# tested the corrections myself. It helped me name the error faster, but I
# still did the actual fixing, so it added to what I understood.
# 


# Exercise 1 
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# Exercise 2 
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# Exercise 3 
# Start at $200, take the gold discount, then add 7% tax on top.
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

after_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)

print(f"final_price(200, \"gold\", 0.07) = ${final_price(200, 'gold', 0.07):.2f}")


# Exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# Exercise 5 
# Fixed version of broken_sales.py. The three bugs were:
#   1. total = sale overwrote the running total every pass, so it ended
#      at 90 instead of adding up. Changed it to total += sale.
#   2. for sale in sales was missing the colon, which is a SyntaxError.
#      Added the colon.
#   3. while i <= len(sales) ran one step too far. len is 5 but the last
#      valid index is 4, so sales[5] crashed with IndexError. Changed the
#      <= to < so it stops in range.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale              # fix 1: add, don't overwrite
print(f"Total: ${total}")

count = 0
for sale in sales:             # fix 2: added the missing colon
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):          # fix 3: < instead of <= so we stay in range
    print(sales[i])
    i += 1


# Exercise 6 
# Prediction: 100, then 1998, then 100 again.
# The x inside double_it() is its own local variable. Assigning x = 999 in
# there builds a separate name that only exists during the call, so it
# never touches the global x = 100. The function returns 999 * 2, which is
# 1998, and the global x is still 100 after the call runs. The lesson is
# that a name defined inside a function stays inside that function unless
# you tell Python otherwise with the global keyword.
x = 100   # global variable

def double_it():
    x = 999   # local variable, separate from the global x
    return x * 2

print(x)           # 100
print(double_it()) # 1998
print(x)           # 100, still unchanged
