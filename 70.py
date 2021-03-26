# пример создания декоратора
import time


def my_timer(f):
    def tmp(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        delta_time = time.time() - start_time
        print(f"Время выполнения функции: {delta_time}")
        return result

    return tmp


@my_timer
def my_sum(a, b, c):
    return a + b + c


print(my_sum(3, 5, 77))
