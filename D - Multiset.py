def solve(n, x, y):
    if sum(x) != sum(y):
        return -1
    x.sort()
    y.sort()
    diff_sum = 0
    #print(x,y)
    for i in range(len(x)):
        diff_sum += abs(x[i] - y[i])/2
    return int(diff_sum)


# ---------- I/O ----------
if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(solve(n, x, y))
