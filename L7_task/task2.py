'''
Задание 2
Напишите функцию, в которую задаётся год в виде числа. 
Нужно определить, есть ли в этом году пятница, 13-е. 
Организуйте вывод всех пятниц 13-х в виде списка.
'''
from datetime import datetime

def find_friday_13(year):
    # Список для хранения дат пятниц 13-го
    fridays_13 = []
    
    # Перебираем все месяцы в году
    for month in range(1, 13):
        # Создаем объект datetime для 13-го числа каждого месяца
        date = datetime(year, month, 13)
        
        # Проверяем, является ли день недели пятницей (пятница = 4, согласно документации Python)
        if date.weekday() == 4:
            # Добавляем дату в список, если это пятница 13-е
            fridays_13.append(date.strftime("%d.%m.%Y"))
    
    return fridays_13

# Основная программа

if __name__ == '__main__':
    # Пример использования функции
    year = 2024
    fridays_13_list = find_friday_13(year)
    print(f"В {year} году пятницы 13-е выпадают на следующие даты: {fridays_13_list}")  
