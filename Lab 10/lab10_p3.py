# Problem 3

text = input("Enter text to analyze: ")
# Add your code below
letter_counts = {}

for letter in text:
    letter = letter.lower()
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print("Letter counts in the entered text:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")