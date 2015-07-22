N, K = map(int, raw_input().split(' '))
R = sorted(map(int, raw_input().split(' ')))[::-1]

C = 0.
for k in range(K-1, -1, -1):
  C = (C + R[k]) / 2.
print C
