# Blacksmith - 21/11/26

# Variables
SWORD_PRICE = 45

sword_discount = 0
guild_discount = 0
delivery = 15
sword_discount_ten = 10
sword_discount_twenty = 20
what_sword_discount = ""
what_guild_discount = ""
what_delivery = ""
purchase = ""


# Input
sword_number = int(input("How many sword do you want ? : "))
guild_member = input("Are you a member of the guild ? (y/n): ")
player_gold = int(input("How many gold do you have ? : "))

# Calculate
total_sword = sword_number * SWORD_PRICE

if sword_number < 5:
    sword_discount = (SWORD_PRICE / 100) * 0
    what_sword_discount = "-0%"
elif sword_number >= 10:
    sword_discount = (total_sword / 100) * 20
    what_sword_discount = "-20%"
elif sword_number >= 5:
    sword_discount = (total_sword / 100) * 10
    what_sword_discount = "-10%"

if guild_member == "y" or guild_member == "yes":
    guild_discount = ((sword_discount - total_sword) / 100) * 5
    what_guild_discount = "-5%"
if guild_member == "n" or guild_member == "no":
    guild_discount = ((sword_discount - total_sword) / 100) * 0
    what_guild_discount = "-0%"

total = int(total_sword - sword_discount - guild_discount)

if total >= 400:
    delivery = 0
    what_delivery = "Free delivery"
if total < 400:
    total += delivery
    what_delivery = "(+15 for the delivery)"

if total <= player_gold:
    purchase_left = player_gold - total
    purchase = f"Purchase possible, you will have {purchase_left}g left."
if total > player_gold:
    purchase_left =  total - player_gold
    purchase = f"Purchase not possible, you will need {purchase_left}g more."

# Display
print(f'''
Base price : {total_sword}
Quantity discount : {what_sword_discount}
Guild discount : {what_guild_discount}
Total: {total} gold, {what_delivery}
{purchase}
''')