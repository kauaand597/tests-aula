def remove_smallest(numbers: list):
    if not numbers:
        return []
    smallest = min(numbers)
    numbers.remove(smallest)
    return numbers