a, b = raw_input().split(' ')

a_int = int(a)
b_int = int(b)
ans = a_int - b_int

for i in range(3):
  for n in range(10):
    if i == 0 and n == 0: continue
    tmp = int(a[:i] + str(n) + a[i+1:]) - b_int
    if tmp > ans: ans = tmp
    tmp = a_int - int(b[:i] + str(n) + b[i+1:])
    if tmp > ans: ans = tmp

print ans


