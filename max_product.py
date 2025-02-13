lst = eval(input("Enter list in []: "))

min1 = 0
min2 = 0
max1 = 0
max2 = 0

for l in lst:
    if l > max2:
        if l > max1:
            max2 = max1
            max1 = l
        else:
            max2 = l
    elif l < min2:
        if l < min1:
            min2 = min1
            min1 = l
        else:
            min2 = l

if min1*min2 < max1*max2:
    print(f"({max1}, {max2})")
else:
    print(f"({min1}, {min2})")