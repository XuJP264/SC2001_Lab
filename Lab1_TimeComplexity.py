from Lab1_HybridMergeSort import traditional_merge_sort
from Lab1_HybridMergeSort import hybrid_merge_sort
from random import randint
import time
import sys
import matplotlib
matplotlib.use('Agg')  # 非交互模式，直接保存
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def arr_generate(min_size, max_size, x):
    times_hybrid = {}
    times_traditional = {}
    counters_hybrid = {}
    counters_traditional = {}
    n = min_size
    while n <= max_size:
        arr = [randint(1, x) for _ in range(n)]
        print(f"Array of size n={n} generated")

        starter = time.perf_counter()
        _, counter2 = traditional_merge_sort(arr.copy())
        ender = time.perf_counter()
        times_traditional[n] = ender - starter
        counters_traditional[n] = counter2
        print(f"Traditional MergeSort completed for n={n}, comparisons={counter2}, time={ender-starter:.4f}s")

        S = 1
        while S <= 128:
            starter = time.perf_counter()
            _, counter1 = hybrid_merge_sort(arr.copy(), S)
            ender = time.perf_counter()
            times_hybrid[(n, S)] = ender - starter
            counters_hybrid[(n, S)] = counter1
            print(f"Hybrid MergeSort completed for n={n}, S={S}, comparisons={counter1}, time={ender-starter:.4f}s")
            S *= 2

        n *= 10
        print(f"All sorts completed for array size n={n//10}\n")
    return times_hybrid,times_traditional,counters_traditional,counters_hybrid
def visualize(times_hybrid, times_traditional, counters_traditional, counters_hybrid):
    print('visualization begin')
    os.makedirs("plots", exist_ok=True)

    fixed_S = 16
    ns = sorted(set(n for n, s in times_hybrid.keys() if s == fixed_S))
    if len(ns) > 100:
        ns_plot = np.logspace(np.log10(ns[0]), np.log10(ns[-1]), 100, dtype=int)
        ns_plot = [n for n in ns_plot if n in ns]
    else:
        ns_plot = ns

    hybrid_count = [counters_hybrid[(n, fixed_S)] for n in ns_plot]
    traditional_count = [counters_traditional[n] for n in ns_plot]

    plt.figure()
    plt.scatter(ns_plot, traditional_count, label='Traditional MergeSort', color='blue')
    plt.scatter(ns_plot, hybrid_count, label=f'Hybrid MergeSort S={fixed_S}', color='red')
    plt.plot(ns_plot, traditional_count, color='blue', alpha=0.3)
    plt.plot(ns_plot, hybrid_count, color='red', alpha=0.3)
    plt.xlabel('Array size n')
    plt.ylabel('Number of key comparisons')
    plt.title(f'Key Comparisons vs Array Size (S={fixed_S})')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.savefig("plots/comparisons_vs_n.png")
    plt.close()

    fixed_n = max(ns)
    Ss = sorted([s for (n, s) in times_hybrid.keys() if n == fixed_n])
    hybrid_count_S = [counters_hybrid[(fixed_n, s)] for s in Ss]

    plt.figure()
    plt.scatter(Ss, hybrid_count_S, label=f'Hybrid MergeSort n={fixed_n}', color='green')
    plt.plot(Ss, hybrid_count_S, color='green', alpha=0.3)
    plt.xlabel('Threshold S')
    plt.ylabel('Number of key comparisons')
    plt.title(f'Key Comparisons vs Threshold S (n={fixed_n})')
    plt.xscale('log', base=2)
    plt.yscale('log')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.savefig("plots/comparisons_vs_S.png")
    plt.close()

    optimal_S_for_n = {}
    for n in ns:
        Ss_n = sorted([s for (nn, s) in times_hybrid.keys() if nn == n])
        counts_n = [counters_hybrid[(n, s)] for s in Ss_n]
        min_index = counts_n.index(min(counts_n))
        optimal_S_for_n[n] = Ss_n[min_index]

    plt.figure()
    plt.scatter(ns, [optimal_S_for_n[n] for n in ns], color='purple')
    plt.plot(ns, [optimal_S_for_n[n] for n in ns], color='purple', alpha=0.3)
    plt.xlabel('Array size n')
    plt.ylabel('Optimal Threshold S')
    plt.title('Optimal S vs Array Size')
    plt.xscale('log')
    plt.grid(True, which="both", ls="--")
    plt.savefig("plots/optimal_S_vs_n.png")
    plt.close()

    largest_n = max(ns)
    best_S = optimal_S_for_n[largest_n]

    plt.figure()
    plt.bar(['Traditional MergeSort', f'Hybrid MergeSort S={best_S}'],
            [counters_traditional[largest_n], counters_hybrid[(largest_n, best_S)]],
            color=['skyblue', 'salmon'])
    plt.ylabel('Number of key comparisons')
    plt.title(f'Comparison at n={largest_n} with optimal S={best_S}')
    plt.grid(axis='y', ls='--')
    plt.savefig("plots/comparison_max_n.png")
    plt.close()

    plt.figure()
    plt.bar(['Traditional MergeSort', f'Hybrid MergeSort S={best_S}'],
            [times_traditional[largest_n], times_hybrid[(largest_n, best_S)]],
            color=['skyblue', 'salmon'])
    plt.ylabel('CPU Time (s)')
    plt.title(f'CPU Time Comparison at n={largest_n} with optimal S={best_S}')
    plt.grid(axis='y', ls='--')
    plt.savefig("plots/time_comparison_max_n.png")
    plt.close()

    print("All plots saved in 'plots' folder.")

if __name__ == "__main__":
    min_size = 1000
    max_size = 10000000
    max_value = 1000000000
    th, tt, ct, ch = arr_generate(min_size, max_size, max_value)
    visualize(th, tt, ct, ch)

