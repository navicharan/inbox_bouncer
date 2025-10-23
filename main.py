```python
import logging

def is_armstrong_number(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError('Input must be a non-negative integer')
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum([int(digit) ** num_digits for digit in num_str])
    return armstrong_sum == number


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        number = int(input('Enter a number to check if it is an Armstrong number: '))
        if is_armstrong_number(number):
            logging.info(f'{number} is an Armstrong number')
        else:
            logging.info(f'{number} is not an Armstrong number')
    except ValueError as e:
        logging.error(f'Error: {e}')


if __name__ == '__main__':
    main()
```