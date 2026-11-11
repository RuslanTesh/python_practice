num = int(input())
seven_letters = 0
total = 0 

while True: # first miss
    if len(str(num)) > 7: # second miss
        seven_letters += 1

    total += 1 # third miss
    if num % 100 == 11:
        break
    num = int(input())

print(seven_letters, '/', total, sep='')