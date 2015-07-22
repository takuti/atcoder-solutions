N, M = map(int, raw_input().split(' '))

mat = [None] * N
for n in range(N):
  mat[n] = [False] * N
  mat[n][n] = True

# create connection matrix
for m in range(M):
  x1, y1 = map(int, raw_input().split(' '))
  mat[x1-1][y1-1] = True
  mat[y1-1][x1-1] = True

# check all possible groups
largest_group = 1
for i in range(1, 2 ** N):

  # get people indices of possible group
  bits = bin(i)[2:].zfill(N)
  people = []
  for j in range(N):
    if bits[j] == '1': people.append(j)

  n = len(people)
  if n <= largest_group: continue

  # check whether the possible group is acceptable
  group_flg = True
  for xi in range(n-1):
    for yi in range(xi+1, n):
      if not mat[people[xi]][people[yi]] and not mat[people[yi]][people[xi]]:
        group_flg = False
        break
    if not group_flg: break

  if group_flg and largest_group < n: largest_group = n

print largest_group
