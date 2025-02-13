fst = int(input("Enter 1st no: "))
sec = int(input("Enter 2nd no: "))

def prime(num):
    for i in range(2, int(num/2)+1):
        if num%i == 0:
            return False
    return True

def check(fst, sec):
    if fst<=0 or sec<=0 or abs(sec - fst) != 2:
        return "Not "
    elif prime(fst) and prime(sec):
        return ""
    else:
        return "Not "
    
print(f"Given two Number are {check(fst, sec)}Twin Prime Number")