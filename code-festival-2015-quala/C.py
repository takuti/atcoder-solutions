def ans():
    N, T = map(int, raw_input().split(' '))

    t = 0
    diff_cnt = [0] * (10 ** 4 + 1)
    max_d = 0
    total = 0
    for i in range(N):
        A, B = map(int, raw_input().split(' '))
        t += A
        d = A - B
        if d > max_d: max_d = d
        diff_cnt[d] += 1
        total += d

    if t - total > T: return -1
    if t <= T: return 0

    cnt = 0
    for d in range(max_d, -1, -1):
        for i in range(diff_cnt[d]):
            if t <= T: break
            t -= d
            cnt += 1

    return cnt

def main():
    print ans()

if __name__ == '__main__':
    main()
