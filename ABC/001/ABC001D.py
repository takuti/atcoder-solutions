N = input()
rains = []

points = []
for i in range(N):
  start, end = map(int, raw_input().split('-'))

  while start % 5 != 0:
    start -= 1

  while end % 5 != 0:
    end += 1
  end_s = '%04d' % end
  if int(end_s[2:]) == 60:
    end = int(str(int(end_s[:2]) + 1) + '00')

  rains.append((start, end))

rains = sorted(list(set(rains)))

ret = []
for rain in rains:
  if len(ret) == 0:
    ret.append(rain)
    continue
  if ret[-1][1] < rain[0]:
    ret.append(rain)
  else:
    s = min(ret[-1][0], rain[0])
    e = max(ret[-1][1], rain[1])
    ret[-1] = (s, e)

for s, e in ret:
  print '%04d-%04d' % (s, e)
