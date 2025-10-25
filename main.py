```python
import logging

logging.basicConfig(level=logging.INFO)

def fibonacci(n):
    if n <= 0:
        logging.error('Input must be a positive integer')
        return None
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
            fib_series.append(b)
        return fib_series

if __name__ == '__main__':
    n = 10
    result = fibonacci(n)
    if result:
        logging.info(f'Fibonacci series of length {n}: {result}')
```