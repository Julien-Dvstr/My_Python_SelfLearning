# Follow the instructions and code - 19/11/26

# Instructions
'''
In this game, the level is determined by experience using the formula: level = integer part of (square root of
(xp / 100)) + 1. The experience required to reach level x is 100 * (x − 1)². Ask for the player's
experience and display their level, the XP required for the next level, and a progress bar consisting of 20
characters between the current level and the next one.

- The bar contains exactly 20 characters between the brackets: "#" for the filled portion, "." for the rest
- The percentage is an integer (truncated)
- Also test with 0 (level 1, empty bar) and 100 (level 2, empty bar)

X - Not allowed : The math module (not covered yet). The square root is calculated using ** 0.5.
'''
MAX_BAR_LENGTH = 20

player_xp = int(input("How much experience do you have? "))
player_level = int((player_xp / 100) ** 0.5) + 1
current_level_xp = 100 * (player_level - 1) ** 2
next_level_xp = 100 * player_level ** 2
xp_to_next_level = next_level_xp - player_xp
progress = int((player_xp - current_level_xp) / (next_level_xp - current_level_xp) * 100)

filled = int((progress / 100) * MAX_BAR_LENGTH)
xp_bar = "#" * filled + "." * (MAX_BAR_LENGTH - filled)

print("Experience:", player_xp)
print("Level:", player_level)
print(f"Next level at {next_level_xp} XP ({xp_to_next_level} to go)")
print(f"[{xp_bar}] {progress}%")
