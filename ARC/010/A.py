N, M, A, B = map(int, raw_input().rstrip().split(' '))

c = [input() for i in range(M)]

have = N
for i in range(M):
    if have <= A: have += B
    have -= c[i]
    if have < 0:
        print (i+1)
        break
    elif i == M-1:
        print 'complete'

