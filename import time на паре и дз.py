import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Время выполнения: {execution_time:.10f} секунд")
        return result
    return wrapper

def repeat(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                print(f"Вывод #{i+1}:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat (n=3)
@timing_decorator
def say_hi(name):
    print(f"Привет, {name}!")
    return "Готово"

print("Итог:")
say_hi("Алиса")