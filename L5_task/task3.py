'''
Задание 3
Создайте и выведите на экран массивы. Получившиеся матрицы сохраните в текстовые файлы.

единичную матрицу размера 5 × 5;
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
    identity_matrix_5x5 = np.eye(5)
    print_and_save(identity_matrix_5x5, 'L5_task/eyes/identity_matrix_5x5.txt')