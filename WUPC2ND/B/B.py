N = input()
S = raw_input()

i = out = 0
while i < N-1:
  for step in range(3,0,-1):
    if i + step >= N: continue
    if S[i+step] != 'X':
      i += step
      break
    elif step == 1:
      out += 1
      i += 3

print out
