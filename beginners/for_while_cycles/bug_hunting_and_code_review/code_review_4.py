count = 0
product = 1 # second mistake

for i in range(1, 11): # first mistake
    num = int(input())
    if num >= 0: # fourth mistake
        product *= num # optimized
        count += 1 # optimized

if count > 0:
    print(count) # third mistake
    print(product)
else:
    print('NO')