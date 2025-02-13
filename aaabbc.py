# input: aaabbc
# output: 3a2b1c

inp = input("Enter: ")

var = inp[0]
count = 0
result = ""

for i in inp:
    if var == i:
        count += 1
    else:
        result += str(count) + var
        var = i
        count = 1
else:
    result += str(count) + var

print(result)