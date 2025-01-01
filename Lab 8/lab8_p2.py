# Problem 2
word1 = "red"
word2 = "scarlet"

# Add your code below
red_count = 0
scarlet_count = 0

textfile = open('scarlet.txt', 'r')
words = textfile.readlines()
for word in words:
    word = word.split(" ")
    if word2 in word:
        scarlet_count = scarlet_count + 1
    if word1 in word:
        red_count = red_count + 1

print ("The word 'scarlet' appears", scarlet_count, "times.")
print ("The word 'red' appears", red_count, "times.")