s1 = input()
s2 = input()
s3 = input()

mx = max(s1, s2, s3)
mn = min(s1, s2, s3)

if s1 != mx and s1 != mn:
    av = s1
elif s2 != mx and s2 != mn:
    av = s2
elif s3 != mx and s3 != mn:
    av = s3
        
print(mn, av, mx)