from typing import Union, Optional

class Calculator:
    def __init__(self) -> None:
        self.last_result: Optional[float] = None

    def add(self, x: Union[int, float], y: Union[int, float]) -> float:
        """Add two numbers."""
        self.last_result = float(x + y)
        return self.last_result

    def subtract(self, x: Union[int, float], y: Union[int, float]) -> float:
        """Subtract y from x."""
        self.last_result = float(x - y)
        return self.last_result

    def multiply(self, x: Union[int, float], y: Union[int, float]) -> float:
        """Multiply two numbers."""
        self.last_result = float(x * y)
        return self.last_result

    def divide(self, x: Union[int, float], y: Union[int, float]) -> float:
        """Divide x by y."""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        self.last_result = float(x / y)
        return self.last_result

    def power(self, x: Union[int, float], y: Union[int, float]) -> float:
        """Calculate x raised to the power of y."""
        self.last_result = float(x ** y)
        return self.last_result

    def square_root(self, x: Union[int, float]) -> float:
        """Calculate the square root of x."""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        self.last_result = float(x ** 0.5)
        return self.last_result

    def percentage(self, x: Union[int, float], y: Union[int, float]) -> float:
        """Calculate what percentage x is of y."""
        if y == 0:
            raise ValueError("Cannot calculate percentage with zero denominator")
        self.last_result = float((x / y) * 100)
        return self.last_result

    def get_last_result(self) -> Optional[float]:
        """Return the last calculated result."""
        return self.last_result
