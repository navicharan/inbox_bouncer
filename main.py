```python
import re

def longest_substring_with_k_vowels(input_str, k):
    if not isinstance(input_str, str) or not isinstance(k, int) or k < 0:
        raise ValueError('Invalid input. Please provide a valid string and a non-negative integer.')
    
    vowels = set('aeiou')
    max_length = 0
    result = ''
    
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str) + 1):
            substring = input_str[i:j]
            vowel_count = sum(1 for char in substring if char.lower() in vowels)
            if vowel_count == k and len(substring) > max_length:
                max_length = len(substring)
                result = substring
    
    return result

# Example Usage
input_str = 'leetcode'
k = 2
print(longest_substring_with_k_vowels(input_str, k))
```