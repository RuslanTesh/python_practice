a, b, c, d = input(), input(), input(), input()
min_s = min(a, b, c, d)
max_s = max(a, b, c, d)

print((ord(min_s[-1]) * ord(max_s[-1])) ** 2)