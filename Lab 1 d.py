from Lab1_HybridMergeSort import traditional_merge_sort, hybrid_merge_sort
from random import randint
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


def compare_final_S_vs_traditional(final_S, n=10_000_000, x=10**6):
    """比较最终S下的Hybrid MergeSort与Traditional MergeSort"""
    os.makedirs("plots", exist_ok=True)

    # 生成一个随机数组
    arr = [randint(1, x) for _ in range(n)]

    # --- Traditional MergeSort ---
    arr_copy = arr.copy()
    start = time.perf_counter()
    _, comps_trad = traditional_merge_sort(arr_copy)
    end = time.perf_counter()
    time_trad = end - start

    # --- Hybrid MergeSort ---
    arr_copy = arr.copy()
    start = time.perf_counter()
    _, comps_hybrid = hybrid_merge_sort(arr_copy, final_S)
    end = time.perf_counter()
    time_hybrid = end - start

    print(f"\nComparison at n={n}")
    print(f"Traditional MergeSort: time={time_trad:.4f}s, comps={comps_trad}")
    print(f"Hybrid MergeSort (S={final_S}): time={time_hybrid:.4f}s, comps={comps_hybrid}")

    # --- 绘制 CPU time 对比 ---
    plt.figure()
    plt.bar(['Traditional MergeSort', f'Hybrid MergeSort S={final_S}'],
            [time_trad, time_hybrid],
            color=['skyblue', 'salmon'])
    plt.ylabel('CPU Time (s)')
    plt.title(f'CPU Time Comparison (n={n}, S={final_S})')
    plt.grid(axis='y', ls='--')
    plt.savefig("plots/finalS_vs_traditional_time.png")
    plt.close()

    # --- 绘制 Key Comparisons 对比 ---
    plt.figure()
    plt.bar(['Traditional MergeSort', f'Hybrid MergeSort S={final_S}'],
            [comps_trad, comps_hybrid],
            color=['skyblue', 'salmon'])
    plt.ylabel('Key Comparisons')
    plt.title(f'Key Comparisons Comparison (n={n}, S={final_S})')
    plt.grid(axis='y', ls='--')
    plt.savefig("plots/finalS_vs_traditional_comparisons.png")
    plt.close()

    print("Plots saved in 'plots' folder: finalS_vs_traditional_time.png and finalS_vs_traditional_comparisons.png")


if __name__ == "__main__":
    # 假设你前面已经得到 avg_S = 最优阈值
    avg_S = 17  # ⚠️ 这里手动填入 find_optimal_S_cpu_time() 得到的结果
    compare_final_S_vs_traditional(avg_S, n=10_000_000, x=10**6)
