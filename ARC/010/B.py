def idx(m, d):
    n = 0
    for i in range(1, m):
        if i == 2: n += 29
        elif i in [4,6,9,11]: n += 30
        else: n += 31
    return n + d - 1

days = [0] * 366
for di in range(366):
    if di % 7 == 0 or di % 7 == 6: days[di] = 1

N = input()
for i in range(N):
    m, d = map(int, raw_input().rstrip().split('/'))
    di = idx(m, d)
    if days[di] == 1:
        try:
            days[di + days[di:].index(0)] = 1
        except:
            continue
    else:
        days[di] = 1

h = 0
max_h = 0
for di in range(366):
    if days[di] == 1:
        h += 1
        if h > max_h: max_h = h
    else:
        h = 0

print max_h
