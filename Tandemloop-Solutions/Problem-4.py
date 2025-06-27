def count_multiples(numbers: list[int]) -> dict[int, int]:
    """Counts multiples of numbers 1-9 in a list."""
    return {i: sum(1 for num in numbers if num % i == 0) for i in range(1, 10)}

if __name__ == "__main__":
    print("\n===== Multiples Counter =====")
    input_str = input("Enter numbers (comma-separated): ")
    numbers = [int(x) for x in input_str.split(",")]
    print("\nCount of multiples:")
    for k, v in count_multiples(numbers).items():
        print(f"{k}: {v}")