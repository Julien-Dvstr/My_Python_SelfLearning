# Fix and explain each bug in a comment - 18/11/26

# Original script
## Variables
#POTION_PRICE = 12
#DISCOUNT = 10

## Script
#quantity = input("How many potions ? ")
#total = quantity * POTION_PRICE
#reduction = total * DISCOUNT / 10
#final = total - reduction
#print("Price: " + final + "coins")

# Corrected Script
# Variables
POTION_PRICE = 12
DISCOUNT = 10

# Script
quantity = int(input("How many potions ? ")) #10
total = quantity * POTION_PRICE
reduction = total * DISCOUNT / 100
final = total - reduction
print(f"Price: {final} coins")