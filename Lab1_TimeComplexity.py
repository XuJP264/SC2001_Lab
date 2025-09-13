from Lab1_HybridMergeSort import traditional_merge_sort
from Lab1_HybridMergeSort import hybrid_merge_sort
import matplotlib.pyplot as plt
from random import randint
import time
import sys
sys.setrecursionlimit(100000)  # 例如增加递归深度

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
        print(f"All sorts completed for array size n={n//100}\n")

    visualize_results(times_hybrid, times_traditional, counters_hybrid, counters_traditional)

def visualize_results(times_hybrid, times_traditional, counters_hybrid, counters_traditional):
    fixed_S = 16
    ns = sorted(set(n for n, s in times_hybrid.keys() if s == fixed_S))
    hybrid_time = [times_hybrid[(n, fixed_S)] for n in ns]
    traditional_time = [times_traditional[n] for n in ns]
    hybrid_count = [counters_hybrid[(n, fixed_S)] for n in ns]
    traditional_count = [counters_traditional[n] for n in ns]

    plt.figure()
    plt.plot(ns, hybrid_time, marker='o', label=f'Hybrid Time S={fixed_S}')
    plt.plot(ns, traditional_time, marker='x', label='Traditional Time')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input size n (log scale)')
    plt.ylabel('Time (seconds, log scale)')
    plt.title(f'Execution Time vs Input Size (S={fixed_S})')
    plt.legend()
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.savefig(f'time_vs_n_S{fixed_S}.png', dpi=300)
    plt.close()

    plt.figure()
    plt.plot(ns, hybrid_count, marker='o', label=f'Hybrid Comparisons S={fixed_S}')
    plt.plot(ns, traditional_count, marker='x', label='Traditional Comparisons')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input size n (log scale)')
    plt.ylabel('Key Comparisons (log scale)')
    plt.title(f'Key Comparisons vs Input Size (S={fixed_S})')
    plt.legend()
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.savefig(f'comparisons_vs_n_S{fixed_S}.png', dpi=300)
    plt.close()

    fixed_n = max(times_traditional.keys())
    Ss = sorted(s for n, s in times_hybrid.keys() if n == fixed_n)
    hybrid_time_S = [times_hybrid[(fixed_n, s)] for s in Ss]
    hybrid_count_S = [counters_hybrid[(fixed_n, s)] for s in Ss]

    plt.figure()
    plt.plot(Ss, hybrid_time_S, marker='o')
    plt.xscale('log', base=2)
    plt.xlabel('Threshold S (log2 scale)')
    plt.ylabel('Time (seconds)')
    plt.title(f'Hybrid MergeSort Time vs Threshold S (n={fixed_n})')
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.savefig(f'time_vs_S_n{fixed_n}.png', dpi=300)
    plt.close()

    plt.figure()
    plt.plot(Ss, hybrid_count_S, marker='o')
    plt.xscale('log', base=2)
    plt.xlabel('Threshold S (log2 scale)')
    plt.ylabel('Key Comparisons')
    plt.title(f'Hybrid MergeSort Key Comparisons vs Threshold S (n={fixed_n})')
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.savefig(f'comparisons_vs_S_n{fixed_n}.png', dpi=300)
    plt.close()



if __name__ == "__main__":
    min_size = 1000
    max_size = 1000000
    max_value = 1000000
    arr_generate(min_size, max_size, max_value)
