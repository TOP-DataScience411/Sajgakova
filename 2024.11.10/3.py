def numbers_strip(numbers: list[float], n: int = 1, return_copy: bool = False) -> list[float]:

    if return_copy:
        numbers = numbers.copy()

    if n > len(numbers):
        return []
        
    for _ in range(n):
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    
    return numbers