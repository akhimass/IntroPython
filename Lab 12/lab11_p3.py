# Problem 3

def get_even(nums):
    uniquenums = []
    for num in nums:
        if num % 2 == 0 and num not in uniquenums:
            uniquenums.append(num)
    return uniquenums

print(get_even([1,4,5,6,5,4]))
