'''
Задание 2
Создайте и выведите на экран массивы. Получившиеся матрицы сохраните в текстовые файлы.

из единиц: одномерные длины 10 и 55, матрицу размерами 3×4, трёхмерный массив формы 2 × 4 × 5;
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
    ones_1d_10 = np.ones(10)
    ones_1d_55 = np.ones(55)
    ones_matrix_3x4 = np.ones((3, 4))
    ones_3d_2x4x5 = np.ones((2, 4, 5))
    print_and_save(ones_1d_10, 'L5_task/ones/ones_1d_10.txt')
    print_and_save(ones_1d_55, 'L5_task/ones/ones_1d_55.txt')
    print_and_save(ones_matrix_3x4, 'L5_task/ones/ones_matrix_3x4.txt')
    print_and_save(ones_3d_2x4x5, 'L5_task/ones/ones_3d_2x4x5.txt')