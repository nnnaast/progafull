import time
import functools

def timing_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнялась {execution_time:.4f} секунд")
        return result
    
    return wrapper

def calculate_sum(n):
    """Вычисляет сумму списка"""
    return sum(n)

@timing_decorator
def calculate_sum_decorated(n):
    return sum(n)

numbers = list(range(1_000_000))
result = calculate_sum_decorated(numbers)
print(f"Сумма: {result}")
