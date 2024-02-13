# Задание 3
# Считайте текстовый файл «Телефоны.txt». Найдите в нём любой номер телефона (вводится с клавиатуры) и выведите адрес, по которому расположен этот телефон, на экран.

class ContactList:
    contacts: dict[str,str] = dict()
    
    def __init__(self, file_location: str):
        with open(file_location, 'r') as file:
            fileinfo = file.read()
            file_lines = fileinfo.replace('<','').replace('>','').splitlines()
            for file_line in file_lines:
                contact_info = file_line.split('\t')
                self.contacts[contact_info[3]] = f"Улица {contact_info[0]}, дом {contact_info[1]}, квартира {contact_info[2]}"
                
    def find_by_phone_number(self, phone_number: str):
        print(self.contacts.get(phone_number, "Номер не найден!"))
        
    
if __name__ == '__main__':
    cl = ContactList("Телефоны.txt")
    looking_for_number = input("Какой номер ищем: ")
    cl.find_by_phone_number(looking_for_number)
    