num, base = map(int, input().strip().split(' '))
print(sum(map(lambda x: int(x[1]) * base ** x[0], enumerate(str(num)[::-1]))))
