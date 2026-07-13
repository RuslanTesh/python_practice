fs = int(input())

prev = 0
fib = 1

for _ in range(fs):
    print(fib, end=" ")
    temp = fib
    fib += prev
    prev = temp
