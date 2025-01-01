# Problem 4
user_input = str(input("Please enter a word: "))
words = open("words5000.csv", "r")

for line in words:
    line = line.split(",")
    if user_input in line:
        print("The word", user_input, "is one of the 5000 common english words.")
    else:
        print("The word", user_input, "is not one of the 5000 common english words.")