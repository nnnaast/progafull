import logging
import functools
from datetime import datetime

def log_args(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        call_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        result = func(*args, **kwargs)
        
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"Время вызова: {call_time}\n")
            f.write(f"Имя функции: {func.__name__}\n")
            f.write(f"Аргументы: позиционные={args}, именованные={kwargs}\n")
            f.write(f"Возвращаемое значение: {result}\n")
            f.write("-" * 40 + "\n")
        
        return result
    
    return wrapper

@log_args
def add(a, b):
    return a + b

@log_args
def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

print(add(5, 3))
print(greet("Алиса", greeting="Здравствуй"))
