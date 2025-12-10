import math
import sys

def stats_from_file(filename):
    with open(filename, "r") as f:
        numbers = list(map(float, f.read().split()))

    if not numbers:
        raise ValueError("File contains no numbers")

    n = len(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    mean = sum(numbers) / n

    # Population standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / (n - 1)
    std_dev = math.sqrt(variance)

    return min_val, max_val, mean, std_dev


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python stats.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    min_v, max_v, avg, std = stats_from_file(filename)

    print(f"Min: {min_v}")
    print(f"Max: {max_v}")
    print(f"Average: {avg}")
    print(f"Standard Deviation: {std}")

