# Input: hye
# Output: h,y,e,hy,ye,hye

string = input("Enter: ")
lst = []
for i in range(len(string)):
    for j in range(i+1, len(string)+1):
        lst.append(string[i:j])

print(','.join(lst))