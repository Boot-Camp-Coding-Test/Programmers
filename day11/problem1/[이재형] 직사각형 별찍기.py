a, b = map(int, input().strip().split(' '))
x = []
x.append('*'*a)
x.append('\n')
x = x*b
print(''.join(x))
