import random
import time
import matplotlib.pyplot as plt

# ---------------- Comparison Counter ----------------
class ComparisonCounter:
    def __init__(self):
        self.count = 0

    def add(self, n=1):
        self.count += n

# ---------------- Insertion Sort（原地） ----------------
def insertion_sort_inplace(arr, left, right, counter: ComparisonCounter):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left:
            counter.add()
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key

# ---------------- Merge（原地辅助数组） ----------------
def merge_inplace(arr, left, mid, right, counter: ComparisonCounter):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        counter.add()
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1
    # 写回原数组
    arr[left:right+1] = temp

# ---------------- Hybrid MergeSort（原地索引版） ----------------
def hybrid_mergesort_inplace(arr, left, right, S, counter: ComparisonCounter):
    if right - left + 1 <= S:
        insertion_sort_inplace(arr, left, right, counter)
        return
    mid = (left + right) // 2
    hybrid_mergesort_inplace(arr, left, mid, S, counter)
    hybrid_mergesort_inplace(arr, mid + 1, right, S, counter)
    merge_inplace(arr, left, mid, right, counter)

# ---------------- Data Generation ----------------
def generate_data(n, max_val=None):
    if max_val is None:
        max_val = n
    return [random.randint(1, max_val) for _ in range(n)]

# ---------------- Experiments ----------------
if __name__ == "__main__":
    # 比较不同 S 值
    n = 200_000
    arr = generate_data(n)
    S_values = [2, 4, 8, 16, 32, 64, 128]
    comp_S = []
    for S in S_values:
        arr_copy = arr[:]
        counter = ComparisonCounter()
        hybrid_mergesort_inplace(arr_copy, 0, len(arr_copy)-1, S, counter)
        comp_S.append(counter.count)
        print(f"S={S}, comparisons={counter.count}")

    plt.plot(S_values, comp_S, marker="o")
    plt.xlabel("S (threshold)")
    plt.ylabel("Comparisons")
    plt.title(f"Hybrid mergesort comparisons vs S (n={n})")
    plt.show()

    # 大数组性能测试
    n = 10_000_000
    arr = generate_data(n)
    arr_copy = arr[:]
    counter = ComparisonCounter()
    start = time.time()
    hybrid_mergesort_inplace(arr_copy, 0, len(arr_copy)-1, S=32, counter=counter)
    t_hybrid = time.time() - start
    print(f"Hybrid mergesort (S=32) on {n} elements time: {t_hybrid:.2f}s, comparisons: {counter.count}")
