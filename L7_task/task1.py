'''
Задание 1
Напишите функцию, которая будет принимать дату в строковом формате и возвращать дату на неделю позже. Примечания:

функция и принимает, и возвращает строку
дата должна иметь формат день.месяц.год
'''
from datetime import datetime, timedelta

def add_week_to_date(date_str):
    # Парсим строку в объект datetime
    date_format = "%d.%m.%Y"
    date_obj = datetime.strptime(date_str, date_format)
    
    # Добавляем неделю к дате
    new_date_obj = date_obj + timedelta(weeks=1)
    
    # Возвращаем новую дату в строковом формате
    new_date_str = new_date_obj.strftime(date_format)
    return new_date_str




# Основная программа

if __name__ == '__main__':
    # Пример использования функции
    input_date = "25.02.2024"
    new_date = add_week_to_date(input_date)
    print(f"Исходная дата: {input_date}, дата через неделю: {new_date}")