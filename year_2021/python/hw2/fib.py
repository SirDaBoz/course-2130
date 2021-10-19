
def fibonacci(prev=0, next=1):
    """
    # Задание 4

    Написать генератор чисел Фибоначчи

    Input:
    ```

    ```

    Output:
    ```
        next call: 0
        next call: 1
        ...
    ```
    """
    while True:
        yield prev
        next, prev = prev + next, next