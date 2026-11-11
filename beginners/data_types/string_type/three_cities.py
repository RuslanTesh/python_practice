n1 = input()
n2 = input()
n3 = input()

len1 = len(n1)
len2 = len(n2)
len3 = len(n3)

min_n = min(len1, len2, len3)
max_n = max(len1, len2, len3)

if min_n == len1:
    print(n1)
elif min_n == len2:
    print(n2)
elif min_n == len3:
    print(n3)

if max_n == len1:
    print(n1)
elif max_n == len2:
    print(n2)
elif max_n == len3:
    print(n3)