D = map(int, raw_input().split(' '))
J = map(int, raw_input().split(' '))

total = 0
for i in range(len(D)):
  total = (total + D[i]) if D[i] >= J[i] else (total + J[i])

print total
