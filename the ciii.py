from Lab1_HybridMergeSort import hybrid_merge_sort
from random import randint
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


def find_optimal_S_cpu_time(num_samples=10, n_min=1000, n_max=1000000, x=10**6):
    """随机选择 n，找到每个 n 的最优 S（CPU time最小），返回结果字典和最终平均 optimal S"""
    np.random.seed(42)
    ns = np.random.randint(n_min, n_max + 1, size=num_samples)

    optimal_S_for_n = {}

    for n in ns:
        best_time = float("inf")
        best_S = None

        arr = [randint(1, x) for _ in range(n)]

        for S in range(2, 41):
            start = time.perf_counter()
            hybrid_merge_sort(arr.copy(), S)
            end = time.perf_counter()
            elapsed = end - start

            if elapsed < best_time:
                best_time = elapsed
                best_S = S

        optimal_S_for_n[n] = best_S
        print(f"n={n}, optimal S={best_S}, best time={best_time:.6f}s")

    # 取平均并取整
    avg_S = int(round(np.mean(list(optimal_S_for_n.values()))))
    print(f"\nFinal optimal S (average of 10 ns) = {avg_S}")

    return optimal_S_for_n, avg_S


def plot_optimal_S(optimal_S_for_n, avg_S):
    """绘制 n vs optimal S 的散点图"""
    os.makedirs("plots", exist_ok=True)

    ns = sorted(optimal_S_for_n.keys())
    Ss = [optimal_S_for_n[n] for n in ns]

    plt.figure()
    plt.scatter(ns, Ss, color='purple', label='Optimal S per n')
    plt.axhline(avg_S, color='red', linestyle='--', label=f'Average Optimal S = {avg_S}')
    plt.xscale('log')
    plt.xlabel('Array size n (log scale)')
    plt.ylabel('Optimal S')
    plt.title('Optimal Threshold S vs Array Size n')
    plt.legend()
    plt.grid(True, ls='--')
    plt.savefig("plots/optimal_S_vs_n.png")
    plt.close()
    print("Plot saved as plots/optimal_S_vs_n.png")


if __name__ == "__main__":
    optimal_S_for_n, avg_S = find_optimal_S_cpu_time(num_samples=10, n_min=1000, n_max=1000000, x=10**6)
    plot_optimal_S(optimal_S_for_n, avg_S)
