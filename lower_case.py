string = input("Enter: ")
output = ""

for s in string:
    asc = ord(s)
    if asc>=65 and asc<=95:
        output += chr(asc+32)
    else:
        output += chr(asc)

print(output)