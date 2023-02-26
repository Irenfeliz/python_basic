# put your python code here
col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

x1 = col1 % 2
y1 = row1 % 2

x2 = col2 % 2
y2 = row2 % 2

color1 = 0
color2 = 0

if x1 != 0 and y1 != 0:
    color1 = 1
elif x1 == 0 and y1 == 0:
    color1 = 1
else:
    color1 = 0
print(x1, y1, color1)

if x2 != 0 and y2 != 0:
    color2 = 1
elif x2 == 0 and y2 == 0:
    color2 = 1
else:
    color2 = 0   

print(x2, y2, color1)

if color1 == color2:
    print('YES')
else:
    print('NO')