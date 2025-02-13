# input: a2b3c4
# output: aabbbcccc

inp = input("Enter: ")

b = ""

[a:=i if i.isalpha() else (b:=b+(a*int(i))) for i in inp]

print(b)

