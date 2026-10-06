s = input().split()
string = '+'.join(s)
sum = sum([int(i) for i in s])


print(string, '=', sum, sep='')