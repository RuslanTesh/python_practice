s = 0 # third mistake

for i in range(1, 8): # first mistake
    n = int(input()) # second mistake
    if n % 2 == 0: # fourth mistake
        s += n # optimized

print(s)