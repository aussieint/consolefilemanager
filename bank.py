def bank():
    balans = 0
    history = []

    while True:
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
                history.append((good, cost))
        elif choice == '3':
            print(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
