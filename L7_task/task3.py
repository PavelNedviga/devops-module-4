'''
Задание 3
Напишите функцию которая принимает datetime, значение аргумента по умолчанию укажите текущуюю дату и время. Фукнция должна вернуть три строки:

количество дней до Нового года
Количество дней до пятницы 13-го (будующей до конца года), при наличии
Количество дней до лета (при наличии), если уже лето, то можно это сообщить.
'''
from datetime import datetime, timedelta

def time_until_events(current_date=datetime.now()):
    # Новый год
    new_year_date = datetime(current_date.year + 1, 1, 1)
    days_until_new_year = (new_year_date - current_date).days

    # Пятница 13-го
    friday_13_message = "Пятница 13-го в этом году не осталась."
    for month in range(current_date.month, 13):
        possible_friday_13 = datetime(current_date.year, month, 13)
        if possible_friday_13 > current_date and possible_friday_13.weekday() == 4:
            days_until_friday_13 = (possible_friday_13 - current_date).days
            friday_13_message = f"До ближайшей пятницы 13-го осталось {days_until_friday_13} дней."
            break

    # До лета
    summer_start_date = datetime(current_date.year, 6, 1)
    if current_date >= summer_start_date and current_date <= datetime(current_date.year, 8, 31):
        summer_message = "Сейчас лето!"
    elif current_date > datetime(current_date.year, 8, 31):
        summer_message = "Лето уже закончилось."
    else:
        days_until_summer = (summer_start_date - current_date).days
        summer_message = f"До лета осталось {days_until_summer} дней."

    return f"До Нового года осталось {days_until_new_year} дней.", friday_13_message, summer_message




if __name__ == '__main__':
    current_date = datetime.now()  # Можно указать конкретную дату для проверки
    # Пример использования функции
    days_until_new_year, next_friday_13, days_until_summer = time_until_events(current_date)
    print(days_until_new_year)
    print(next_friday_13)
    print(days_until_summer)
    # Основная программа
