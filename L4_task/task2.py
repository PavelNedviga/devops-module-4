# Задание 2
# Создайте (откройте на запись) текстовый файл «Телефоны.txt». Запишите в него информацию в следующем формате: <<Улица Дом Квартира Номер телефона>>. Данные вводите с клавиатуры. Запрашивайте у пользователя необходимую информацию, пока не введёте 10 номеров. При записи в файл в качестве разделителя между столбцами используйте табуляцию (’\t’) или пробел (’␣’).
from dataclasses import dataclass

@dataclass
class Contact:
    street: str = None
    house: str = None
    flat: str = None
    phone_number: str = None
    def __init__(self, street, house, flat, phone_number):
        self.street = street
        self.house = house
        self.flat = flat
        self.phone_number = phone_number
        
    def __str__(self) -> str:
        return self.__repr__()
       
    def __repr__(self) -> str:
        return f"<<{self.street}\t{self.house}\t{self.flat}\t{self.phone_number}>>"
    

if __name__ == '__main__':
    num = int(input("кол-во записей: "))
    with open('Телефоны.txt', "w") as file:        
        for i in range(num):            
            user = Contact(input("Введите улицу: "), input("Введите номер дома: "), input("Введите номер квартиры: "), input("Введите телефон: "))
            print()
            file.write(str(user) + "\n")