import time
import random
import numpy as np
import matplotlib.pyplot as graph  

# Iterative Fibonacci (fastest for large n)
def fibonacci_iterative(n):
    if n < 2:
        return [0] if n == 1 else [0, 1]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Recursive Fibonacci (inefficient for large n)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Memoized Fibonacci (caching for speedup)
def fibonacci_memoized(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

# Matrix exponentiation method (O(log n) time complexity)
def fibonacci_matrix(n):
    def multiply_matrices(A, B):
        return np.dot(A, B).astype(int)

    def matrix_power(matrix, exp):
        result = np.identity(len(matrix), dtype=int)
        while exp:
            if exp % 2:
                result = multiply_matrices(result, matrix)
            matrix = multiply_matrices(matrix, matrix)
            exp //= 2
        return result

    if n == 0:
        return 0
    base_matrix = np.array([[1, 1], [1, 0]], dtype=int)
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0, 0]

# Function to check if a number is in Fibonacci sequence
def is_fibonacci_number(n):
    x1 = 5 * (n ** 2) + 4
    x2 = 5 * (n ** 2) - 4
    return int(x1 ** 0.5) ** 2 == x1 or int(x2 ** 0.5) ** 2 == x2

# Function to generate a Fibonacci-based pseudo-random number
def fibonacci_random(n):
    sequence = fibonacci_iterative(n)
    return random.choice(sequence)

# Function to compute golden ratio using Fibonacci sequence
def golden_ratio(n):
    sequence = fibonacci_iterative(n)
    return sequence[-1] / sequence[-2] if len(sequence) > 1 else 1

# Function to express a number as a sum of non-consecutive Fibonacci numbers (Zeckendorf’s theorem)
def fibonacci_sum_representation(n):
    sequence = fibonacci_iterative(50)[::-1]  # Generate and reverse Fibonacci sequence
    result = []
    for num in sequence:
        if num <= n:
            n -= num
            result.append(num)
        if n == 0:
            break
    return result

# Function to measure execution time of different Fibonacci methods
def measure_time(method, n):
    start = time.time()
    if method == "recursive":
        sequence = [fibonacci_recursive(i) for i in range(n)]
    elif method == "memoized":
        sequence = [fibonacci_memoized(i) for i in range(n)]
    elif method == "matrix":
        sequence = [fibonacci_matrix(i) for i in range(n)]
    else:
        sequence = fibonacci_iterative(n)
    return sequence, time.time() - start

# Function to plot Fibonacci growth and golden ratio approximation
def plot_fibonacci_growth(n):
    sequence = fibonacci_iterative(n)
    ratios = [sequence[i+1] / sequence[i] for i in range(1, len(sequence) - 1)]

    graph.plot(ratios, marker='o', linestyle='-', color='green', markersize=6, label="Golden Ratio Approximation")
    graph.axhline(y=1.618, color='red', linestyle='--', label="Theoretical Golden Ratio (1.618)")
    graph.title('Golden Ratio Approximation in Fibonacci Sequence')
    graph.xlabel('Index')
    graph.ylabel('Ratio')
    graph.legend()
    graph.grid(True)
    graph.show()

# Main function
def main():
    n = 30  # Number of Fibonacci numbers to generate

    # Measure execution time of different methods
    iter_seq, iter_time = measure_time("iterative", n)
    memo_seq, memo_time = measure_time("memoized", n)
    matrix_seq, matrix_time = measure_time("matrix", n)

    # Recursive method is slow, only run for small n
    if n <= 20:
        rec_seq, rec_time = measure_time("recursive", n)
    else:
        rec_seq, rec_time = [], float('inf')

    # Print results
    print("Iterative:", iter_seq, f"Time: {iter_time:.6f} sec")
    print("Memoized:", memo_seq, f"Time: {memo_time:.6f} sec")
    print("Matrix:", matrix_seq, f"Time: {matrix_time:.6f} sec")
    if rec_seq:
        print("Recursive:", rec_seq, f"Time: {rec_time:.6f} sec")

    # Check if a number is in Fibonacci sequence
    num_to_check = 34
    print(f"Is {num_to_check} a Fibonacci number?", is_fibonacci_number(num_to_check))

    # Generate a Fibonacci-based pseudo-random number
    random_fib = fibonacci_random(n)
    print(f"Random Fibonacci number: {random_fib}")

    # Calculate and print the golden ratio approximation
    phi = golden_ratio(n)
    print(f"Golden Ratio approximation: {phi}")

    # Fibonacci sum representation
    num_to_represent = 45
    representation = fibonacci_sum_representation(num_to_represent)
    print(f"Zeckendorf Representation of {num_to_represent}: {representation}")

    # Plot Fibonacci growth
    plot_fibonacci_growth(n)

if __name__ == "__main__":
    main()