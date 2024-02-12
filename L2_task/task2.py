# Задание 2
# Напишите функцию, которая принимает аргумент – список целых чисел A и возвращает 2 списка: нечетных и четных чисел из A.
# Пример: [1, 2, 3, 4, 5] Возврат: ([1, 3, 5], [2, 4])

def split_odd_even(numbers):
    # Разделение списка на четные и нечетные числа
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    return odd_numbers, even_numbers


if __name__ == '__main__':
    example_list = [1, 2, 3, 4, 5]
    # Демонстрация работы функции с примером списка
    odd_numbers, even_numbers = split_odd_even(example_list)
    print(odd_numbers,even_numbers)