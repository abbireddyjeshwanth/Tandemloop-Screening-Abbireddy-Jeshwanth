class AdvancedCalculator:
    """
    A professional calculator with error handling and interactive input.
    Operations: +, -, *, /
    """
    def compute(self, a: float, b: float, op: str) -> float:
        op = op.lower().strip()
        if op in ("add", "+", "addition"):
            return a + b
        elif op in ("subtract", "-", "subtraction"):
            return a - b
        elif op in ("multiply", "*", "multiplication"):
            return a * b
        elif op in ("divide", "/", "division"):
            if b == 0:
                raise ZeroDivisionError("Error: Division by zero!")
            return a / b
        else:
            raise ValueError("Invalid operation!")

if __name__ == "__main__":
    calc = AdvancedCalculator()
    print("===== Advanced Calculator =====")
    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))
        op = input("Choose the operation (+, -, *, /): ")
        result = calc.compute(a, b, op)
        print(f"\nRESULT: {a} {op} {b} = {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except ZeroDivisionError as e:
        print(e)