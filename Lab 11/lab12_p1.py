# Problem #1

# Loop A
n = 0
while n < 3:
    print(n)
    n += 1



# Loop B
i = 0
while i < 3:
    j = 0
    while j < i + 1:
        print("*", end="")
        j += 1
    print("!")
    i += 1
print()
