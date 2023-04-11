# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def add_cont():
    file = open('файл.txt', 'a', encoding='UTF-8')
    data1 = input('введите ФИО: ')
    data2 = input('номер телефона: ')
    data3 = input('комментарий: ')
    data = '\n' + data1 + '; ' + data2 + '; ' + data3
    print(data)
    file.write(data)
    file.close()
    print('контакт добавлен')


def read_cont():
    file = open('файл.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    print('Вот список контактов:\n')
    for contact in data:
        print(contact)

def find_cont():
    file = open('файл.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    search_cont = input('введите для поиска информацию: ')
    print('Вот найденный контакт:')
    for cont in data:
        if search_cont.lower() in cont.lower():
            print(cont)
            return   
    print("Контакт не найден")

def change_cont():
    phone_book = []
 
    file = open('файл.txt', 'r+', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        new_contact = contact.strip().split(';')
        new_contact1 = {'name': new_contact[0],
                        'phone': new_contact[1],
                        'comment': new_contact[2]}
        phone_book.append(new_contact1)


    print("Введите ФИО контакта, который хотите изменить: ")
    name = input("> ")

    for contact in phone_book:
        if contact['name'].lower() == name.lower():
            print("Контакт найден. Хотите изменить ФИО? да/нет: ")
            answer = input("> ")
            if answer.lower() == "да":
                print("Введите новое ФИО: ")
                new_name = input("> ")
                contact['name'] = new_name
            print("Хотите изменить номер телефона? да/нет: ")
            answer = input("> ")
            if answer.lower() == "да":
                print("Введите новый номер телефона: ")
                new_phone = input("> ")
                contact['phone'] = new_phone
            print("Хотите изменить комментарий? да/нет: ")
            answer = input("> ")
            if answer.lower() == "да":
                print("Введите новый комментарий: ")
                new_comment = input("> ")
                contact['comment'] = new_comment
            new_phone_book = []

            for contact in phone_book:
                new_contact = '; '.join([values for values in contact.values()])
                new_phone_book.append(new_contact)

            new_phone_book = '\n'.join(new_phone_book)
            print("Контакт успешно изменен")
            file = open('файл.txt', 'w', encoding='UTF-8')
            file.write(new_phone_book)
            file.close()      
            return
    print('Контакт не найден')
            
def for_delete():
    file = open('файл.txt', 'r+', encoding='UTF-8')
    data = file.readlines()
    file.close()
    name = input('введите контакт для удаления: ')
    for contact in data:
        if name.lower() == contact.split(';')[0].lower():
            print("Вы хотите удалить контакт (да/нет)?: " + name )
            name_del = input('> ')
            if name_del == 'да':
               data.remove(contact) 
               print("Вы удалили контакт " + name)
               file = open('файл.txt', 'w', encoding='UTF-8')
               file.write(''.join(data))
               file.close()
               return
    print("Такого контакта нет " + name)
                

choosing_actions = int(input('введите цифру:\n 1. Добавить контакт\n 2. Вывести список контактов\n 3. Найти определенный контакт \n 4. Изменить данные контакта\n 5. Удалить контакт\n -> '))
if choosing_actions == 1:
    add_cont()
elif choosing_actions == 2:
    read_cont()
elif choosing_actions == 3:
    find_cont()
elif choosing_actions == 4:
    change_cont()
elif choosing_actions == 5:
    for_delete()