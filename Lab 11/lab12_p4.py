# Problem #4
# Add your code here
distance1 = int(input("Enter the amount of distance you are able to run right now."))
enddistance = int(input("Enter the amount of distance you want to be able to run. "))

def daystoreachgoal(distance1, enddistance):
    days = 0
    currentdistance = distance1
    while currentdistance < enddistance:
        currentdistance *= 1.1
        days += 1
    return days

print("Number of days needed to reach the goal:", daystoreachgoal(distance1 , enddistance))
