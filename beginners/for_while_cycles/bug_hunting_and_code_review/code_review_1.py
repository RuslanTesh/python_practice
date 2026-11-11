n = int(input()) # first mistake
product = 1 # second mistake

while n != 0: # third mistake
    digit = n % 10
    product *= digit #optimized
    n //= 10
    
print(product)