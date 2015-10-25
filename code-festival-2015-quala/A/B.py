n = input()
A = map(int, raw_input().split(' '))

s = A[n-1]
for i in range(n-2, -1, -1):
    s += A[i] * (2 ** (n - 2 - i)) * 2

print s
