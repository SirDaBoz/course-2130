import time


def call_controller(n_calls: int, time_interval: int):
    """
    Напишите функцию декоратор, которая ограничивает количество вызовов функции.

    ```
    n_calls: количество возможнх вызовов
    time_interval: время в секундах
    ```

    ```
    @firewall(10, 20):
    def foo():
      pass
    ```
    """
    count = [0]

    def decorator(fn):
        def function(*args, **kwargs):
            time.sleep(time_interval)
            if count[0] < n_calls:
                count[0] += 1
                return fn(*args, **kwargs)
            else:
                return
        return function
    return decorator


def call_rectifier(func1, func2, func3, func4):
    """
    Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
        1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
        2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """
    funcs = [func1, func2, func3, func4]
    for func in funcs:
        try:
            func()
        except Exception:
            continue
        return func
    return RuntimeError
