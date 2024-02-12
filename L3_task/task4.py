'''
Задание 4
Определите суперкласс Сотрудник, включающий:

конструктор, инициализирующий имя работника, его должность (по умолчанию None) и оклад (по умолчанию 0);
метод экземпляра для повышения оклада на какую-то часть (например, на 0.3, т.е. на 30%) с округлением результата до копеек;
магический метод str для перегрузки строкового представления объекта, который должен выводить данные о работнике в формате 'Атрибут: объект.атрибут' по одной записи на каждой строке. Также определите подкласс Менеджер, наследующий суперкласс Сотрудник и переопреоделяющий метод повышения оклада таким образом, чтобы он еще больше повышал оклад за счет дополнительного бонуса в виде к акой-то части оклада. Далее:
создайте экземпляр иван_менеджер созданного подкласса с начальным окладом в 1700 рублей;
повысьте сотруднику оклад за счет стандартной надбавки в 0.335 и бонуса за должность в 0.25;
выведите строковое представление объекта экземпляра с информацией о сотруднике на экран.
'''

class Сотрудник:
    имя: str 
    должность: str
    оклад: float
    def __init__(self, name, position=None, salary=0):
        self.имя = name
        self.должность = position
        self.оклад = salary

    def повысить_оклад(self, part):
        self.оклад += self.оклад * part
        self.оклад = round(self.оклад, 2)

    def __str__(self):
        return f'Имя: {self.имя}\nДолжность: {self.должность}\nОклад: {self.оклад} руб.'

class Менеджер(Сотрудник):
    def повысить_оклад(self, часть, бонус=0):
        super().повысить_оклад(часть + бонус)


        
if __name__ == '__main__':
    # Создание экземпляра иван_менеджер с начальным окладом в 1700 рублей
    иван_менеджер = Менеджер("Иван", "Менеджер", 1700)
    # Повышение оклада на стандартную надбавку и бонус за должность
    иван_менеджер.повысить_оклад(0.335, 0.25)
    # Вывод информации о сотруднике
    print(иван_менеджер)