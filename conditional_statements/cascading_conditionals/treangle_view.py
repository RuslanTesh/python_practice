a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Равносторонний')
elif a == b != c or a != b == c or a == c != b:
    print('Равнобедренный')
else:
    print('Разносторонний')