def factorial(n):
  result = 1
  for i in xrange(n,1,-1):
    result *= i
  return result

def combination(n, k):
  return factorial(n) / (factorial(n-k) * factorial(k))

N, K = map(int, raw_input().split(' '))

if N <= K:
  d = K / N
  a = K % N
  l = []
  for i in xrange(N):
    if i < a: l.append(d+1)
    else: l.append(d)
  m = combination(N, a) * combination(N - l.count(d+1), N - a)
else:
  m = factorial(N-1+K) / (factorial(N-1) * factorial(K))

print m % 1000000007
