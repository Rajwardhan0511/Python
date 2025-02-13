num = int(input("Enter: "))
fst = 0
sec = 1

if num<=0:
    print("Number should be positive")
elif num==1:
    print(fst)
else:
    for i in range(num):
        print(fst, end=" ")
        sec, fst = fst+sec, sec

