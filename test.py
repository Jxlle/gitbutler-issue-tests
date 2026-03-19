import random
import math


def roll_dice(sides: int = 6) -> int:
    return random.randint(1, sides)


def shuffle_string(s: str) -> str:
    chars = list(s)
    random.shuffle(chars)
    return "".join(chars)


def pick_random_item(items: list):
    return random.choice(items) if items else None


def random_float_between(low: float, high: float) -> float:
    return low + (high - low) * random.random()


def reverse_words(text: str) -> str:
    return " ".join(word[::-1] for word in text.split())


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def clamp(value: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(value, max_val))


def count_vowels(text: str) -> int:
    return sum(1 for c in text.lower() if c in "aeiou")
