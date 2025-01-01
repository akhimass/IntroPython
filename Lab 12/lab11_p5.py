# Problem 5
# add your code here
def word_count(sentence):
    words = sentence.split()
    return len(words)

# Test the function
sentence = "From a programmer’s point of view the user is a peripheral that types when you issue a read request"

print("Number of words:", word_count(sentence))