'''
Задание 4

Создайте и выведите на экран массивы. Получившиеся матрицы сохраните в текстовые файлы.

диагональную матрицу размера 5 × 5, все значения на главной диагонали которой равны 0.5.
'''

import numpy as np
import pickle

# Функция для вывода и сохранения массивов
def print_and_save(array, filename):
    print(array)
    # На 3д не сработал
    np.savetxt(filename, array, fmt='%s') 
    # Сохраняем массив в файл с помощью pickle
    # with open(filename, 'wb') as f:
    #     pickle.dump(array, f)

# Основная программа

if __name__ == '__main__':
    # Создание единичной матрицы размера 5x5
    # Создание диагональной матрицы размера 5x5 с 0.5 на диагонали
    diagonal_matrix_5x5 = np.diag([0.5] * 5)
    print_and_save(diagonal_matrix_5x5, 'L5_task/diag/diagonal_matrix_5x5.txt')