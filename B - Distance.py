def solve(n, k, x):
    x.sort()
    def can_place(d):
        count = 1
        last = x[0]

        for i in range(1, n):
            if x[i] - last >= d:
                count += 1
                last = x[i]
                if count >= k:
                    return True
        return False
    left, right = 1, x[-1] - x[0]
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        if can_place(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
if __name__ == "__main__":
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    print(solve(n, k, x))
