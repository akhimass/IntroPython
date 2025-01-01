# Problem #3
def smallest_factor(n):
    if n < 1:
        return 0
    else:
        factor = 2
        while factor * factor <= n:
            if n % factor == 0:
                return factor
        factor += 1
    return n




# Verify everything works as intended
factor = int(input("Enter a number that is greater than 0: "))
print(smallest_factor(factor))
    