# Problem #2

def squares_less_than_n(n):
    if n < 1:
        print("Parameter value must be greater than 0")
    elif n == 1:
        print(1)
    else:
        i = 1
        while i * i <= n:
            print(i * i)
            i += 1





# Verify everything works as intended
value = 50
squares_less_than_n(value) # this should display the values 1 4 9 16 25 36 49