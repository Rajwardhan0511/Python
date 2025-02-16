# Input = 'abcaba'
# output = 'abcaabbaaa'

str1 = "abcaba"
my_dict = {}
output = ""

for ch in str1:
    if ch in my_dict:
        my_dict[ch] += 1
    else:
        my_dict[ch] = 1
    
    output += ch*my_dict[ch]

print(output)