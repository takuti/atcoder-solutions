
def check(S, T):
  possible = ['a', 't', 'c', 'o', 'd', 'e', 'r']
  for i in range(len(S)):
    if S[i] == T[i]: continue
    elif S[i] == '@' and T[i] in possible: continue
    elif T[i] == '@' and S[i] in possible: continue
    return False
  return True

S = raw_input()
T = raw_input()

if check(S, T): print 'You can win'
else: print 'You will lose'
