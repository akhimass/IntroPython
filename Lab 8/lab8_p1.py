# Problem 1
x_coordinate = []
y_coordinate = []

# Add your code below
fileref = open('xy.txt', 'r')
lines = fileref.readlines()
for line in lines:
    data = line.split(",")
    x = float(data[0])
    y = float(data[1])
    x_coordinate.append(x)
    y_coordinate.append(y_coordinate)

print(len(x_coordinate))
print (len(y_coordinate))
print(type(x_coordinate[0]))
print (type(y_coordinate[1]))