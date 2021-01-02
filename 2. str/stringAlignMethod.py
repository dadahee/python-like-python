s, n = input().strip().split(' ')
n = int(n)

print(s + " " * (n-len(s)))
print(" " * ((n - len(s))//2) + s + " " * ((n - len(s))//2) )
print(" " * (n-len(s)) + s)