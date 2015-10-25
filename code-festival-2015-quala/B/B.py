def ans():
    N, M = map(int, raw_input().split(' '))
    half = N / 2

    cnt = [0] * 10 ** 5
    A = map(int, raw_input().split(' '))

    for a in A:
        cnt[a-1] += 1
        if cnt[a-1] > half: return a

    return '?'

print ans()
