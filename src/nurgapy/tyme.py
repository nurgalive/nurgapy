import time


def tyme(some_function):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = some_function(*args, **kwargs)
        total_time = round(time.perf_counter() - start_time, 2)
        print(f"Function {some_function.__name__}{args} Took {total_time:.2f} seconds")
        return result

    return wrapper
