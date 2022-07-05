import os
import json


def bank():
    balans = 0
    orders = []
    if os.path.exists('balans.txt'):
        with open('balans.txt', 'r') as f:
            balans = int(f.read())
    if os.path.exists('orders.json'):
        with open('orders.json', 'r') as f:
            orders = json.load(f)


    while True:
        print(f'На счету {balans}')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            add_money = int(input('На сколько пополнить счёт? '))
            balans += add_money
        elif choice == '2':
            cost = int(input('Введите сумму покупки: '))
            if cost > balans:
                print('Не хватает')
            else:
                balans -= cost
                good = input('Введите название товара: ')
                orders.append([good, cost])
        elif choice == '3':
            print(orders)
        elif choice == '4':
            with open('orders.json', 'w') as f:
                json.dump(orders, f)
            with open('balans.txt', 'w') as f:
                f.write(str(balans))
            break
        else:
            print('Неверный пункт меню')


if __name__ == "__main__":
    bank()
