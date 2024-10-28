x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())


hor = ''
ver = ''

if x < x1:
    hor = 'W'
elif x > x2:
    hor = 'E'
else:
    hor = ''

if y > y2:
    ver = 'N'
elif y < y1:
    ver = 'S'
else:
    ver = ''

if hor and ver:
    print(ver+hor)
elif hor:
    print(hor)
elif ver:
    print(ver)