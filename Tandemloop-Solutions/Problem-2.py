def generate_odd_series(n: int) -> str:
    """Generates comma-separated odd numbers up to 'n' terms."""
    series = [str(2 * i + 1) for i in range(n)]
    return ", ".join(series)

if __name__ == "__main__":
    print("\n===== Odd Number Series =====")
    n = int(input("Enter a number (n): "))
    print(f"First {n} odd numbers: {generate_odd_series(n)}")