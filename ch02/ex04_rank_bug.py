# Find and correct the bug - 21-11-26

kills = int(input("Monster defeated: "))
if kills >= 100:
    rank = "Legend"
elif kills >= 50:
    rank = "Expert"
elif kills >= 10:
    rank = "Hunter"
elif kills >= 0:
    rank = "Novice"
else:
    rank = "Error"
print(f"Rank : {rank}")

# Original code
'''
kills = int(input("Monster defeated: "))
if kills >= 10:
    rank = "Hunter"
elif kills >= 50:
    rank = "Expert"
elif kills >= 100:
    rank = "Legend"
elif kills <= 0:
    rank = "Error"
else:
    rank = "Novice"
print(f"Rank : {rank}")
'''