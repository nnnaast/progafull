#первая практика 2 курс 2 семестр
#задание на паре сами и в итоге домой: создайте функцию, вычисляющую сумму списка. декорируйте ее так, чтобы получить время ее ввполненния

import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция выполнена за {execution_time:.10f} секунд")
        return result
    return wrapper

@timing_decorator
def calculate_sum(numbers):
    return sum(numbers)

my_list = [1557577577, 23635, 3353553, 43838, -5676666]
print("Сумма:", calculate_sum(my_list))

'''
import time
def decorator(f):
    def w(x):
        start = time.time()
        r = f(x)
        print("Время выполнения: ", time.time() - start)
        return r
    return w

@decorator
def summa(l):
    return sum(l)

print("Сумма: ", summa([1.35535, 20350503505303503, 3, 4, 5]))'''
