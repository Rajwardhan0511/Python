num = int(input("Enter: "))

def fac(num):
    if num==1:
        return 1
    return num*fac(num-1)

print(f"Factoriral of {num} is {fac(num)}")