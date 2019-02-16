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
        new_seeds = num_seeds + random.radiant(4,8)
    num_seeds = new_seeds - num_seeds
    return num_seeds


def distribution_seeds():
    pass


def start_war():
    pass


def conquest_territory():
    costs = random.radiant(2000, 4500)
    new_Territory = random.radiant(4, 10)
    dead_people = random.radiant(2, 20)
    new_people = random.radiant(1, 25)
    people = new_people - dead_people
    seeds = int(math.ceil(new_people * 0.5))
    result_conquest = []
    result_conquest.append(costs)
    result_conquest.append(new_Territory)
    result_conquest.append(people)
    result_conquest.append(seeds)
    return result_conquest


def enlarge_army():
    pass


def taxes(population, army):
    money = (population - army) * 10
    return money


# TODO: ситуация

# TODO: вызов функций
while POPULATION > 0 and DISTEMPER <= 0.65 and ARMY_DISTEMPER <= 0.5 and TERRITORY > 0:
    print('Народ: {}\nКазна: {}\nЗерно: {}\nСмута: {}\nЗемля: {}\nАрмия: {}\nСмута в армии: {}\nМесяц: {}\n'
          'Год: {}\n'.format(POPULATION, MONEY, SEEDS, DISTEMPER, TERRITORY, ARMY, ARMY_DISTEMPER, MONTH, YEAR))

    sale_seeds()

    buy_seeds()

    if MONTH == 1:
        new_SEADS = sowing_seeds(int(input('Сколько зерна засеять')))

    distribution_seeds()

    if MONTH % 2 == 0:
        start_war()

    if MONTH % 4 == 0:
        results = conquest_territory()

    if MONTH % 3 == 0:
        enlarge_army()

    taxes(POPULATION, ARMY)

# TODO: считывание

# TODO: операции
