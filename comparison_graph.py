#!/usr/bin/env python3
"""
Create a comparison graph showing key comparisons for Insertion Sort vs Merge Sort
against input size n, similar to the provided reference graph.
"""

import numpy as np
import matplotlib.pyplot as plt
from Lab1_HybridMergeSort import traditional_merge_sort, traditional_insert_sort
import time


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
        for trial in range(5):  # 5 trials per n
            # Use numpy for deterministic random generation
            arr = np.random.randint(1, max_val + 1, size=n).tolist()
            arrays.append(arr)
        data[n] = arrays

    return data


def measure_comparisons(data):
    """Measure key comparisons for both algorithms."""
    merge_sort_comparisons = []
    insertion_sort_comparisons = []

    for n in sorted(data.keys()):
        merge_comps = []
        insertion_comps = []

        for arr in data[n]:
            # Measure merge sort
            _, merge_comp = traditional_merge_sort(arr.copy())
            merge_comps.append(merge_comp)

            # Measure insertion sort
            _, insertion_comp = traditional_insert_sort(arr.copy())
            insertion_comps.append(insertion_comp)

        # Store average comparisons
        merge_sort_comparisons.append(np.mean(merge_comps))
        insertion_sort_comparisons.append(np.mean(insertion_comps))

    return merge_sort_comparisons, insertion_sort_comparisons


def create_comparison_graph(n_values, merge_comparisons, insertion_comparisons, output_file="comparison_graph.png"):
    """Create the comparison graph similar to the reference."""

    # Set up the plot
    plt.figure(figsize=(12, 8))
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['savefig.dpi'] = 300

    # Plot the lines
    plt.plot(n_values, merge_comparisons, 'b-', linewidth=2.5, label='Mergesort', marker='o', markersize=6)
    plt.plot(n_values, insertion_comparisons, 'orange', linewidth=2.5, label='Insertion Sort', marker='s', markersize=6)

    # Crossover point analysis removed as requested

    # Customize the plot
    plt.xlabel('Input Size (n)', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Key Comparisons', fontsize=14, fontweight='bold')
    plt.title('No. of Key Comparisons against Input Size for Mergesort & Insertion Sort',
              fontsize=16, fontweight='bold', pad=20)

    # Set axis limits and ticks
    plt.xlim(0, max(n_values) * 1.05)
    plt.ylim(0, max(max(merge_comparisons), max(insertion_comparisons)) * 1.1)

    # Add grid
    plt.grid(True, alpha=0.3, linestyle='--')

    # Add legend
    plt.legend(loc='upper left', fontsize=12, framealpha=0.9)

    # Statistics text removed as requested

    # Tight layout and save
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')

    print(f"Graph saved as {output_file}")


def main():
    """Main function to generate the comparison graph."""
    print("Generating Insertion Sort vs Merge Sort Comparison Graph")
    print("=" * 60)

    # Define input sizes to test (similar to reference graph range)
    n_values = list(range(1, 26))  # n from 1 to 25, similar to reference

    print(f"Testing input sizes: n = {min(n_values)} to {max(n_values)}")

    # Generate test data
    print("Generating test data...")
    data = generate_test_data(n_values)

    # Measure comparisons
    print("Measuring key comparisons...")
    merge_comparisons, insertion_comparisons = measure_comparisons(data)

    # Create the graph
    print("Creating comparison graph...")
    create_comparison_graph(n_values, merge_comparisons, insertion_comparisons)

    # Print summary table
    print(f"\nSUMMARY TABLE")
    print(f"{'n':>4} {'Mergesort':>12} {'Insertion':>12} {'Difference':>12}")
    print(f"{'-' * 45}")

    for i, n in enumerate(n_values):
        merge_comp = merge_comparisons[i]
        insertion_comp = insertion_comparisons[i]
        diff = insertion_comp - merge_comp
        print(f"{n:>4} {merge_comp:>12.0f} {insertion_comp:>12.0f} {diff:>12.0f}")

    print(f"\nAnalysis complete!")


if __name__ == "__main__":
    main()
