# Fill-in-the-blank code - 19/11/26

# Blank code
'''
p1_name, p1_score, p1_accuracy = "Zelda", 9850, 0.873
p2_name, p2_score, p2_accuracy = "Link", 12400, 0.9125
print(f"{'Player':<10}|{'Score':>6}|{'Acc.':>7}")
print("-" * 25)
print(f"{p1_name:___}|{p1_score:___}|{p1_accuracy * 100:___}%")
print(f"{p2_name:___}|{p2_score:___}|{p2_accuracy * 100:___}%")
'''

# Answer
p1_name, p1_score, p1_accuracy = "Zelda", 9850, 0.873
p2_name, p2_score, p2_accuracy = "Link", 12400, 0.9125
print(f"{'Player':<10}|{'Score':>6}|{'Acc.':>7}")
print("-" * 25)
print(f"{p1_name:<10}|{p1_score:>6}|{p1_accuracy * 100:>6.1f}%")
print(f"{p2_name:<10}|{p2_score:>6}|{p2_accuracy * 100:>6.1f}%")