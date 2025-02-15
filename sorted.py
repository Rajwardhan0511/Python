def my_fun(data):
    return data[1]

data = [[100, 200], [200, 1000], [150, 10]]

print(sorted(data, key=my_fun, reverse=True))