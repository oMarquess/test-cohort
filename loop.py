def count_to_five() -> list[int]:
    """Demonstrates a simple for loop by generating numbers from 1 to 5."""
    numbers = []
    for i in range(1, 6):
        numbers.append(i)
    return numbers

def countdown(start: int) -> list[int]:
    """Demonstrates a while loop by counting down to 0."""
    result = []
    current = start
    while current >= 0:
        result.append(current)
        current -= 1
    return result

def sum_even_numbers(numbers: list[int]) -> int:
    """Demonstrates loops and conditional logic by summing only even numbers in a list."""
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

if __name__ == "__main__":
    print("For Loop Demonstration:")
    print("Counting to 5:", count_to_five())

    print("\nWhile Loop Demonstration:")
    print("Counting down from 3:", countdown(3))

    print("\nConditional Loop Demonstration:")
    test_list = [1, 2, 3, 4, 5, 6]
    print(f"Sum of even numbers in {test_list}:", sum_even_numbers(test_list))
