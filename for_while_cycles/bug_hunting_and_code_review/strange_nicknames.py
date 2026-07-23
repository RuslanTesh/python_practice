s = input()

while len(s) < 10: # first mistake
    if len(s) % 4 == 0: # second mistake
        s += 'x' # optim
    elif len(s) % 5 == 0: # third mistake
        s += 'y' # optim
    else:
        s = 'z' + s # five miss

s = '@' + s # fourth miss
print(s)