l = input()
s = raw_input()

if (l - 1) % 2 != 0: print -1
else:
  a = 'b'
  K = (l-1)/2
  n = 0
  for i in range(1, K+1):
    if i == 3 * n + 1: a = 'a' + a + 'c'
    elif i == 3 * n + 2: a = 'c' + a + 'a'
    elif i % 3 == 0:
      a = 'b' + a + 'b'
      n += 1
  if s == a: print K
  else: print -1




