def modified_odd_series(n: int) -> str:
    """Generates odd numbers up to the nearest odd count."""
    terms = n if n % 2 != 0 else n - 1
    series = [str(2 * i + 1) for i in range(terms)]
    return ", ".join(series)

if __name__ == "__main__":
    print("\n===== Modified Odd Series =====")
    n = int(input("Enter a number (n): "))
    print(f"Series: {modified_odd_series(n)}")