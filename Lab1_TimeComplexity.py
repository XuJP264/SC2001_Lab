from Lab1_HybridMergeSort import traditional_merge_sort, hybrid_merge_sort
from random import randint
import time
import os
import numpy as np
import matplotlib

matplotlib.use('Agg')  # 非交互模式，直接保存
import matplotlib.pyplot as plt

def find_optimal_S(times_hybrid, counters_hybrid):
    """
    对每个 n，找到最优 S（以平均比较次数为准）。
    每个 n 下有10个数组 -> 10次实验的optimal S，最后取平均后四舍五入。
    """
    ns = sorted(set(n for n, s in times_hybrid.keys()))
    optimal_S_final = {}

    for n in ns:
        # 每个 n 的所有 S
        Ss = sorted([s for (nn, s) in times_hybrid.keys() if nn == n])

        # 每个 n 我们有 repeat 次实验（10个数组 * repeat次），这里求平均
        counts_n = [counters_hybrid[(n, s)][0] for s in Ss]

        # 找最优 S
        best_S = Ss[np.argmin(counts_n)]
        optimal_S_final[n] = best_S

    return optimal_S_final


def find_optimal_S_by_multiple_trials(times_hybrid, counters_hybrid, repeat=10):
    """
    对每个 n，10 组数组，每组找到最优 S，然后取平均并取整。
    """
    ns = sorted(set(n for n, s in times_hybrid.keys()))
    optimal_S_final = {}

    for n in ns:
        Ss = sorted([s for (nn, s) in times_hybrid.keys() if nn == n])
        # 对于每组实验，找到最优 S
        best_S_trials = []
        for trial in range(repeat):
            counts_trial = [counters_hybrid[(n, s)][0] for s in Ss]
            best_S = Ss[np.argmin(counts_trial)]
            best_S_trials.append(best_S)

        # 平均并取整
        avg_S = round(np.mean(best_S_trials))
        optimal_S_final[n] = avg_S

    return optimal_S_final


def plot_optimal_S(optimal_S_final):
    """绘制 n vs optimal S"""
    os.makedirs("plots", exist_ok=True)

    ns = sorted(optimal_S_final.keys())
    Ss = [optimal_S_final[n] for n in ns]

    plt.figure()
    plt.plot(ns, Ss, marker='o', linestyle='-', color='purple')
    plt.xscale('log')  # n 很大时用 log 坐标更直观
    plt.xlabel('Array size n (log scale)')
    plt.ylabel('Optimal S')
    plt.title('Optimal Threshold S vs Array Size n')
    plt.grid(True, ls='--')
    plt.savefig("plots/optimal_S_vs_n.png")
    plt.close()
    print("Optimal S vs n plot saved as plots/optimal_S_vs_n.png")

def generate_test_data(n_values, max_val=1000000, seed=36):
    """Generate test data for different input sizes."""
    # Set both numpy and random seeds for complete determinism
    np.random.seed(seed)
    import random
    random.seed(seed)

    data = {}

    for n in n_values:
        # Generate multiple arrays for each n to get average
        arrays = []
        for trial in range(10):  # 10 trials per n
            # Use numpy for deterministic random generation
            arr = np.random.randint(1000, max_val + 1, size=n).tolist()
            arrays.append(arr)
        data[n] = arrays

    return data
def arr_generate(min_size, max_size, x, repeat=5):

    times_hybrid = {}
    times_traditional = {}
    counters_hybrid = {}
    counters_traditional = {}
    n = min_size
    while n <= max_size:
        print(f"\nArray size n={n}")

        times_list, counters_list = [], []
        for _ in range(repeat):
            arr = [randint(1, x) for _ in range(n)]
            starter = time.perf_counter()
            _, counter2 = traditional_merge_sort(arr.copy())
            ender = time.perf_counter()
            times_list.append(ender - starter)
            counters_list.append(counter2)
        times_traditional[n] = (np.mean(times_list), np.std(times_list))
        counters_traditional[n] = (np.mean(counters_list), np.std(counters_list))
        print(f"Traditional MergeSort n={n}, avg comps={counters_traditional[n][0]:.1f}, avg time={times_traditional[n][0]:.4f}s")

        # ---- 混合归并排序 ----
        for S in range(2, 41):
            times_list, counters_list = [], []
            for _ in range(repeat):
                arr = [randint(1, x) for _ in range(n)]
                starter = time.perf_counter()
                _, counter1 = hybrid_merge_sort(arr.copy(), S)
                ender = time.perf_counter()
                times_list.append(ender - starter)
                counters_list.append(counter1)
            times_hybrid[(n, S)] = (np.mean(times_list), np.std(times_list))
            counters_hybrid[(n, S)] = (np.mean(counters_list), np.std(counters_list))
            print(f"Hybrid MergeSort n={n}, S={S}, avg comps={counters_hybrid[(n,S)][0]:.1f}, avg time={times_hybrid[(n,S)][0]:.4f}s")

        n *= 10

    return times_hybrid, times_traditional, counters_traditional, counters_hybrid


def visualize(times_hybrid, times_traditional, counters_traditional, counters_hybrid):
    print('Visualization begin')
    os.makedirs("plots", exist_ok=True)

    ns = sorted(set(n for n, s in times_hybrid.keys()))

    # 绘制不同 n 的不同 S 的 key comparisons 和 CPU time
    for n in ns:
        Ss = sorted([s for (nn, s) in times_hybrid.keys() if nn == n])
        hybrid_counts_mean = [counters_hybrid[(n, s)][0] for s in Ss]
        hybrid_counts_std = [counters_hybrid[(n, s)][1] for s in Ss]
        hybrid_times_mean = [times_hybrid[(n, s)][0] for s in Ss]
        hybrid_times_std = [times_hybrid[(n, s)][1] for s in Ss]

        # Key comparisons vs S (带误差条)
        plt.figure()
        plt.errorbar(Ss, hybrid_counts_mean, yerr=hybrid_counts_std, marker='o', color='green', capsize=4)
        plt.xlabel('Threshold S')
        plt.ylabel('Number of key comparisons')
        plt.title(f'Hybrid MergeSort Key Comparisons vs S (n={n})')
        plt.grid(True, ls='--')
        plt.savefig(f"plots/comparisons_vs_S_n{n}.png")
        plt.close()

        # CPU time vs S (带误差条)
        plt.figure()
        plt.errorbar(Ss, hybrid_times_mean, yerr=hybrid_times_std, marker='o', color='orange', capsize=4)
        plt.xlabel('Threshold S')
        plt.ylabel('CPU Time (s)')
        plt.title(f'Hybrid MergeSort CPU Time vs S (n={n})')
        plt.grid(True, ls='--')
        plt.savefig(f"plots/time_vs_S_n{n}.png")
        plt.close()

    # 对比传统排序和混合排序的最优 S (以比较次数为标准)
    optimal_S_for_n = {}
    for n in ns:
        Ss_n = sorted([s for (nn, s) in times_hybrid.keys() if nn == n])
        counts_n = [counters_hybrid[(n, s)][0] for s in Ss_n]
        min_index = counts_n.index(min(counts_n))
        optimal_S_for_n[n] = Ss_n[min_index]

    largest_n = max(ns)
    best_S = optimal_S_for_n[largest_n]

    # 比较最优混合排序和传统排序的 key comparisons
    plt.figure()
    plt.bar(['Traditional MergeSort', f'Hybrid MergeSort S={best_S}'],
            [counters_traditional[largest_n][0], counters_hybrid[(largest_n, best_S)][0]],
            yerr=[counters_traditional[largest_n][1], counters_hybrid[(largest_n, best_S)][1]],
            color=['skyblue', 'salmon'], capsize=6)
    plt.ylabel('Number of key comparisons')
    plt.title(f'Comparison at n={largest_n} with optimal S={best_S}')
    plt.grid(axis='y', ls='--')
    plt.savefig("plots/comparison_max_n.png")
    plt.close()

    # 比较最优混合排序和传统排序的 CPU time
    plt.figure()
    plt.bar(['Traditional MergeSort', f'Hybrid MergeSort S={best_S}'],
            [times_traditional[largest_n][0], times_hybrid[(largest_n, best_S)][0]],
            yerr=[times_traditional[largest_n][1], times_hybrid[(largest_n, best_S)][1]],
            color=['skyblue', 'salmon'], capsize=6)
    plt.ylabel('CPU Time (s)')
    plt.title(f'CPU Time Comparison at n={largest_n} with optimal S={best_S}')
    plt.grid(axis='y', ls='--')
    plt.savefig("plots/time_comparison_max_n.png")
    plt.close()

    print("All plots saved in 'plots' folder.")


if __name__ == "__main__":
    min_size = 1000
    max_size = 1000000  # 可调整，避免时间过长
    max_value = 1000000000
    th, tt, ct, ch = arr_generate(min_size, max_size, max_value, repeat=5)  # repeat 次数可调
    visualize(th, tt, ct, ch)
