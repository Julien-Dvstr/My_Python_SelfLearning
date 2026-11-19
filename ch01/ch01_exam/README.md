# ch01 - Final Exercise

## Character Creator

For this end-of-chapter exercise, I created a small RPG character creator using Python.

The player enters their character's name, title, and strength. The program then calculates the remaining attributes and displays a character sheet in the terminal.

I also tried to make the interface dynamic, so its width adjusts to the character's name and title instead of using a fixed size.

## Instructions

Create a character creator using only the concepts covered in Chapter 01.

The program must:

- Ask for the character's name, title, and strength (0 to 10).
- Calculate agility based on the remaining attribute points.
- Calculate HP, attack, dodge, speed, and power using the provided formulas.
- Display the character's stats in a formatted table.
- Display strength and agility bars containing 10 characters each.

The exercise must be completed without conditions, loops, or custom functions.

## My Solution

[View the Python script](exam01_character_creator.py)

I used constants for the formulas and f-strings to format the character sheet.

Instead of using fixed widths for the entire interface, I calculated the available space based on the length of the character's full name.

The trickiest part was aligning the stats and attribute bars while keeping the borders the same width.

## What I Practiced

- Working with variables and constants.
- Using arithmetic operators and type conversion.
- Handling user input.
- Formatting strings with dynamic widths and alignment.
- Displaying decimal values and percentages.
- Building attribute bars using string multiplication.
- Organizing code into separate sections.

## Code Review

After completing my solution, I asked GPT-6 how it would improve the code.

I kept my original implementation and included its suggested version for comparison.

The alternative uses fixed label widths and prepares formatted values before displaying them, making the layout easier to read and maintain.

Both approaches produce a character sheet, but they handle spacing differently.

---

[Back to Chapter 01](../README.md)