import os, sys, shutil
from bank import bank
from victory import victory

while True:
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Выход')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        new_folder = input('Название папки: ')
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        else:
            print('Папка с таким именем уже существует!')
    elif choice == '2':
        rem_obj = input('Удаляемый файл/папка: ')
        if os.path.isfile(rem_obj):
            os.remove(rem_obj)
            print(f'Файл {rem_obj} удалён!')
        elif os.path.exists(rem_obj):
            os.rmdir(rem_obj)
            print(f'Папка {rem_obj} удалена!')
        else:
            print(f'Файл/папка {rem_obj} не существует!')
    elif choice == '3':
        copy_obj = input('Копируемый файл/папка: ')
        if os.path.isfile(copy_obj) or os.path.exists(copy_obj):
            copy_name = input('Новое название: ')
            shutil.copy(copy_obj, copy_name)
        else:
            print('Файл/папка не найдены!')
    elif choice == '4':
        print("Текущая директория:", os.getcwd())
    elif choice == '5':
        dir_list = [dir for dir in os.listdir() if os.path.isdir(dir)]
        print(dir_list)
    elif choice == '6':
        file_list = [file for file in os.listdir() if os.path.isfile(file)]
        # for file in os.listdir():
        #     if os.path.isfile(file):
        #         file_list.append(file)
        print(file_list)
    elif choice == '7':
        print('Операционная система ', sys.platform)
    elif choice == '8':
        with open('listdir.txt', 'w') as f:
            f.write('files: ')
            for file in os.listdir():
                if os.path.isfile(file):
                    f.write(file + ' ')
            f.write('\ndirs:')
            for dir in os.listdir():
                if os.path.isdir(dir):
                    f.write(dir + ' ')


    elif choice == '9':
        victory()
    elif choice == '10':
        bank()
    elif choice == '11':
        os.chdir(input('Введите новую рабочую директорию: '))
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
