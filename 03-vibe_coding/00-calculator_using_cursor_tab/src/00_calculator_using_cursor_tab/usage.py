from calculator import Calculator

def demonstrate_calculator() -> None:
    """Demonstrate the usage of the Calculator class with various operations."""
    # Initialize calculator
    calc = Calculator()
    print("Calculator initialized!")
    print("-" * 30)

    # Basic arithmetic operations
    print("Basic Arithmetic Operations:")
    print(f"Addition: 2 + 3 = {calc.add(2, 3)}")
    print(f"Subtraction: 5 - 2 = {calc.subtract(5, 2)}")
    print(f"Multiplication: 4 * 3 = {calc.multiply(4, 3)}")
    print(f"Division: 10 / 2 = {calc.divide(10, 2)}")
    print("-" * 30)

    # Advanced operations
    print("Advanced Operations:")
    print(f"Power: 2 ^ 3 = {calc.power(2, 3)}")
    print(f"Square Root: √16 = {calc.square_root(16)}")
    print(f"Percentage: 25 is {calc.percentage(25, 100)}% of 100")
    print("-" * 30)

    # Using last result
    print("Using Last Result:")
    calc.add(10, 20)  # Last result will be 30
    print(f"Last result: {calc.get_last_result()}")
    print(f"Using last result in new calculation: {calc.multiply(calc.get_last_result(), 2)}")
    print("-" * 30)

    # Error handling examples
    print("Error Handling Examples:")
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Division by zero error: {e}")

    try:
        calc.square_root(-4)
    except ValueError as e:
        print(f"Negative square root error: {e}")

    try:
        calc.percentage(25, 0)
    except ValueError as e:
        print(f"Percentage with zero denominator error: {e}")

if __name__ == "__main__":
    demonstrate_calculator() 