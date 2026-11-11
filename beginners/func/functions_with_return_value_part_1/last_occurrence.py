def get_last_index(data, value):
    res = 'ERROR!'
    for el in range(len(data)):
        if data[el] == value:
            res = el
    return res


data = eval(input())
value = eval(input())

print(get_last_index(data, value))
