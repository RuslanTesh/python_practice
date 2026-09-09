n = int(input())

for i in range(1, n + 1):
    s = input()
    if s.isspace() or s == '':
        print(i, ': ', 'COMMENT SHOULD BE DELETED', sep='')
    else:
         print(i, ': ', s, sep='')