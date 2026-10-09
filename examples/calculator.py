"""Math helpers for practice; real-valued calculations only."""
import math
import statistics
from prime_numbers import is_prime

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def square_root(value: float) -> float:
    if value < 0:
        raise ValueError("This demo accepts real square roots only.")
    return math.sqrt(value)

def cube_root(value: float) -> float:
    return math.copysign(abs(value) ** (1 / 3), value)

def summarize(values: list[float]) -> dict[str, float | list[float]]:
    if not values or not all(math.isfinite(value) for value in values):
        raise ValueError("Provide a nonempty list of finite numbers.")
    return {"mean": statistics.mean(values), "median": statistics.median(values),
            "modes": statistics.multimode(values), "population_variance": statistics.pvariance(values),
            "population_standard_deviation": statistics.pstdev(values)}

if __name__ == "__main__":
    print(divide(10, 2))
    print(square_root(49))
    print(cube_root(-27))
    print(math.lcm(0, 0))
    print(is_prime(17))
    print(summarize([1, 2, 3, 4]))
