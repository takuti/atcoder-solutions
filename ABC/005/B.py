N = input()
min_T = float('inf')
for i in xrange(N):
  T = input()
  if min_T > T: min_T = T
print min_T

