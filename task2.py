import sys


sys.stdout.reconfigure(encoding='utf-8')

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            return (iterations, upper_bound)
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо не знайшли точний збіг, повертаємо найменший елемент більший за ціль
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return (iterations, upper_bound)

# Тестування функції
sorted_array = [1.1, 2.3, 3.5, 4.8, 5.9, 7.0, 8.2]
target_value = 6.0
result = binary_search(sorted_array, target_value)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
