import math

def is_prime(n):
  """ Return whether given number is prime, or not based on the trial division
  >>> is_prime(41)
  True
  >>> is_prime(40)
  False
  """
  for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
    if n % i == 0:
      n /= i
      return False
  return True

N = input()
if is_prime(N): print 'YES'
else: print 'NO'
