# Problem 3

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

# Add your code below
with open('months.txt', 'w') as file:
    for month in months:
        file.write(month + "\n")
print (months)