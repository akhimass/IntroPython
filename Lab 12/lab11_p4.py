# Problem 4
# add your code here
def get_min_even(lst, num):
    result = []
    for item in lst:
        if item % 2 == 0 and item > num:
            if item not in result:
                result.append(item)
    return result

print(get_min_even([1,4,5,6,5,4], 4))