# Use of the debug tool - 19/11/26

xp = 250
kills = 7
xp_per_kill = 35
bonus = kills * xp_per_kill
xp += bonus
xp_needed = 500 - xp
progress = xp / 500 * 100
print(f"XP: {xp}/500 ({progress:.1f}%), {xp_needed} still needed")

# Questions & Answers

# What is the value of bonus at the breakpoint | xp += bonus | ? What is its type?
# 245 is the value of bonus, type int

# Move down one line. What is the value of xp?
# 495

# Before executing the line `progress = ...`, use `Evaluate Expression` to calculate `xp / 500`. What is the type of the result?
# 0.99, type float

# What is the final value of `xp_needed`? What does this sign mean?
# 5 xp is needed