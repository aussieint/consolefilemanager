import random


def victory():
    numbers = [x for x in range(10)]
    QUETIONS_COUNT = 5
    quetions_numbers = random.sample(numbers, QUETIONS_COUNT)
    birthdays = {
        'Pushkin': '06.06.1799',
        'Lermontov': '15.10.1814',
        'Nekrasov': '28.11.1821',
        'Gogol': '01.04.1809',
        'Blok': '28.11.1880',
        'Esenin': '03.10.1895',
        'Gorkiy': '28.03.1868',
        'Fet': '05.12.1820',
        'Tolstoy': '09.09.1828',
        'Turgenev': '09.11.1818'
    }
    days = {
        '01': 'первое',
        '02': 'второе',
        '03': 'третье',
        '04': 'четвёртое',
        '05': 'пятое',
        '06': 'шестое',
        '07': 'седьмое',
        '08': 'восьмое',
        '09': 'девятое',
        '10': 'десятое',
        '11': 'одиннадцатое',
        '12': 'двенадцатое',
        '13': 'тринадцатое',
        '14': 'четырнадцатое',
        '15': 'пятнадцатое',
        '16': 'шеснадцатое',
        '17': 'семнадцатое',
        '18': 'восемнадцатое',
        '19': 'девятнадцатое',
        '20': 'двадцатое',
        '21': 'двадцать первое',
        '22': 'двадцать второе',
        '23': 'двадцать третье',
        '24': 'двадцать четвёртое',
        '25': 'двадцать пятое',
        '26': 'двадцать шестое',
        '27': 'двадцать седьмое',
        '28': 'двадцать восьмое',
        '29': 'двадцать девятое',
        '30': 'тридцатое',
        '31': 'тридцать первое'
    }
    months = {
        '01': 'января',
        '02': 'феврадя',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря'
    }
    more_game = None

    while more_game != 'Нет':
        right_answers = 0
        person = list(birthdays.keys())
        for i in quetions_numbers:
            answer = input(f'День рождения {person[i]}: ')
            if answer == birthdays[person[i]]:
                right_answers += 1
                print('Верно!')
            else:
                date = birthdays[person[i]]
                day, month, year = date.split('.')
                print(days[day], months[month], year)
        print("Количество правильных ответов: ", right_answers)
        print("Количество ошибок: ", QUETIONS_COUNT - right_answers)
        print("Процент правильных ответов: ", right_answers * 100 / QUETIONS_COUNT)
        print("Процент ошибок: ", (QUETIONS_COUNT - right_answers) * 100 / QUETIONS_COUNT)
        more_game = input("Начать игру сначала?")
