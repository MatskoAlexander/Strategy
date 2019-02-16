import random
import math
# TODO: переменные

POPULATION = 2000
MONEY = 70000
SEEDS = 10000
DISTEMPER = 0.02
TERRITORY = 30
ARMY = 500
ARMY_DISTEMPER = 0.00
MORTALITY = 20
FERTILITY = 20
MONTH = 1
YEAR = 1

# TODO: functions


def sale_seeds():
    pass


def buy_seeds():
    pass


def sowing_seeds(num_seeds):            #Функция возвращает прибавку к зерну
    new_seeds = 0
    for i in range(num_seeds):
        new_seeds = new_seeds + random.randint(4,8)
    num_seeds = new_seeds - num_seeds
    return num_seeds


def distribution_seeds():
    pass


def start_war():
    pass


def conquest_territory():
    result_conquest = []
    costs = random.randint(2000, 4500)
    need_seeds = random.randint(40, 100)
    new_Territory = random.randint(0, 5)
    dead_people = random.randint(0, 20)
    new_people = random.randint(0, 25)
    seeds = int(math.ceil(new_people * 0.5))
    people = new_people - dead_people
    result_conquest.append(costs)
    result_conquest.append(need_seeds)
    result_conquest.append(new_Territory)
    result_conquest.append(people)
    result_conquest.append(seeds)
    return result_conquest


def enlarge_army():
    pass


def taxes_and_pay(population, army):
    money = (population - army) * 10
    pay = army * 12
    money = money - pay
    return money


def bad_harvest(new_seeds):
    pass


def attack():
    pass


def many_rats(seeds):
    pass


def revolution():
    pass


def you_ill(month):
    month = month + 1
    return month


def new_hero():
    pass


def treasure():
    pass


def epidemy():
    pass


def refugee():
    pass


# TODO: ситуация

# TODO: вызов функций
results = []

while POPULATION > 0 and DISTEMPER <= 0.65 and ARMY_DISTEMPER <= 0.5 and TERRITORY > 0 and \
        POPULATION / TERRITORY < 1000:
    print('Народ: {}\nКазна: {}\nЗерно: {}\nСмута: {}\nЗемля: {}\nАрмия: {}\nСмута в армии: {}\nМесяц: {}\n'
          'Год: {}\n'.format(POPULATION, MONEY, SEEDS, DISTEMPER, TERRITORY, ARMY, ARMY_DISTEMPER, MONTH, YEAR))

    #sale_seeds()

    #buy_seeds()

    if MONTH == 1 or MONTH == 6:
        new_SEADS = sowing_seeds(int(input('Сколько зерна засеять?\n')))
        #bad_harvest()

    if MONTH == 4 or MONTH == 10:
        SEEDS = SEEDS + new_SEADS

    #distribution_seeds()

    if MONTH % 2 == 0:
        start_war()

    if MONTH % 4 == 0:
        answer2 = str(input('Хотите освоить новые территории?\n1)Да\n2)Нет\n')) #что не работает, если найдёте ошибку буду благодарен (Саша)
        if answer2 == 1 or answer2.lower() == 'да':
            results.extend(conquest_territory())
            print(results)
            MONEY = MONEY - results[0]
            SEEDS = SEEDS - results[1]
    if not(MONTH == 3 and YEAR == 1) and MONTH % 4 == 3:
        TERRITORY = TERRITORY + results[2]
        POPULATION = POPULATION + results[3]
        SEEDS = SEEDS + results[4]
        results = []

    if MONTH % 3 == 0:
        enlarge_army()

    new_MONEY = taxes_and_pay(POPULATION, ARMY)

    MONEY = MONEY + new_MONEY

    if MONTH == 12:
        MONTH = 0
        YEAR = YEAR + 1
    MONTH = MONTH + 1


# TODO: считывание

# TODO: операции
