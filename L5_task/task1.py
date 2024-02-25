'''
Задание 1
Создайте и выведите на экран массивы. Получившиеся матрицы сохраните в текстовые файлы.

из нулей: одномерные длины 10 и 55, матрицу размерами 3×4, трёхмерный массив формы 2 × 4 × 5;
'''

import numpy as np
import pickle

# Функция для вывода и сохранения массивов
def print_and_save(array, filename):
    print(array)
    # На 3д не сработал
    # np.savetxt(filename, array, fmt='%s') 
    # Сохраняем массив в файл с помощью pickle
    with open(filename, 'wb') as f:
        pickle.dump(array, f)

# Основная программа

if __name__ == '__main__':
    # Создание массивов из нулей    
    zeros_1d_10 = np.zeros(10)
    zeros_1d_55 = np.zeros(55)
    zeros_matrix_3x4 = np.zeros((3, 4))
    zeros_3d_2x4x5 = np.zeros((2, 4, 5))


    # Вывод и сохранение массивов
    print_and_save(zeros_1d_10, 'L5_task/zeros/zeros_1d_10.txt')
    print_and_save(zeros_1d_55, 'L5_task/zeros/zeros_1d_55.txt')
    print_and_save(zeros_matrix_3x4, 'L5_task/zeros/zeros_matrix_3x4.txt')
    print_and_save(zeros_3d_2x4x5, 'L5_task/zeros/zeros_3d_2x4x5.txt')

