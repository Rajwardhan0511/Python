# Input = 'a=10&b=5&name=Raj'
# Output = {'a': '10', 'b': '5', 'name': 'Raj'}

string = 'a=10&b=5&name=Raj'
lst = []

[lst.append(s.split('=')) for s in string.split('&')]

print(dict(lst))