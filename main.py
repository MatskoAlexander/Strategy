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


def sale_seeds(seeds, money): #Функция возвращает, сколько отбавилось зарна и прибавилось денег
    trading_countries = ["Соседняя страна желает купить у вас зерна, ",
                         "Не хотите ли продать несколько мешков зерна городу N?\n"] #Сюда можно добавить ещё больше разных текстов, их тут два чисто для примера
    print(trading_countries[random.randint(0, len(trading_countries) - 1)])
    course = random.randint(20, 35)
    print("Вам предлагают обмен по курсу: {} зол./мешок".format(course))
    try:  
        seeds_amount = int(input("Сколько мешков продадим?\n"))
    except ValueError:
        seeds_amount = int(input("Введите натуральное число: "))
    if seeds_amount == 0:
          print("Вы отказались торговать. Каждый остался при своём")
    else:
          print("Вы продали {} мешков зерна и получили за это {} золота".format(seeds_amount, seeds_amount * course))
    seeds -= seeds_amount
    money += seeds_amount * course
    return seeds, money



def buy_seeds(seeds, money):
    course = random.randint(20, 35)
    print("Есть возможность купить зерно у соседнего города по курсу: {} зол./мешок.".format(course))
    try:  
        seeds_amount = int(input("Сколько мешков купим?\n"))
    except ValueError:
        seeds_amount = int(input("Введите натуральное число: "))
    if seeds_amount == 0:
          print("Вы отказались торговать. Каждый остался при своём")
    else:
          print("Вы купили {} мешков зерна и запатили за это {} золота".format(seeds_amount, seeds_amount * course))
    seeds += seeds_amount
    money -= seeds_amount * course
    return seeds, money


def sowing_seeds(num_seeds):            #Функция возвращает прибавку к зерну
    new_seeds = 0
    for i in range(num_seeds):
        new_seeds += random.randint(4, 8)
    return new_seeds


def distribution_seeds(seeds, population, distemper, army, army_distemper):
    print("Пора раздавать зерно людям")
    answer_f1 = int(input('Сколько зерна раздать?\n'))
    recommend = math.ceil((population - army) * 0.5) + army
    if answer_f1 < recommend:
        distemper = math.ceil((distemper * population + math.ceil((recommend - answer_f1) * 3 / 4)) / population)
        army_distemper = (army_distemper * army + math.ceil((recommend - answer_f1) * 1 / 4)) / army
        population = population - math.ceil((recommend - answer_f1) / 0.5 * 0.85)
    seeds = seeds - answer_f1
    print("Вы раздали {} мешков зерна народу". format(answer_f1))
    return seeds, population, distemper, army, army_distemper



def start_war():
    pass


def conquest_territory():
    costs = random.randint(2000, 4500)
    need_seeds = random.randint(40, 100)
    new_territory = random.randint(0, 5)
    people = random.randint(0, 25) - random.randint(0, 20)
    seeds = int(math.ceil(people * 0.5))
    return costs, need_seeds, new_territory, people, seeds


def enlarge_army():
    pass


def taxes_and_pay(population, army):
    money = (population - army) * 10
    pay = army * 12
    money -= pay
    return money


def bad_harvest(new_seeds):
    rnd = random.randint(1, 20)
    if rnd == 1:
        new_seeds = new_seeds * (random.randint(60, 80)) / 100
        print('Вас постиг неурожай')
    print('Вы собрали {} зерна'.format(new_seeds))
    return new_seeds


def attack():
    pass


def many_rats(seeds):
    pass


def revolution():
    pass


def you_ill(month):
    print('Вы заболели. Пропуск хода.')
    month += 1
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

while POPULATION > 0 and DISTEMPER <= 0.65 and ARMY_DISTEMPER <= 0.5 and TERRITORY > 0 and \
        POPULATION / TERRITORY < 1000:
    print('\n\nНарод: {}\nКазна: {}\nЗерно: {}\nСмута: {}\nЗемля: {}\nАрмия: {}\nСмута в армии: {}\nМесяц: {}\n'
          'Год: {}\n'.format(POPULATION, MONEY, SEEDS, DISTEMPER, TERRITORY, ARMY, ARMY_DISTEMPER, MONTH, YEAR))

    results_sale = sale_seeds(SEEDS, MONEY)
    SEEDS = results_sale[0]
    MONEY = results_sale[1]

    results_buy = buy_seeds(SEEDS, MONEY)
    SEEDS = results_buy[0]
    MONEY = results_buy[1]


    if MONTH == 1 or MONTH == 6:
        sowing = int(input('Сколько зерна засеять?\n'))
        new_SEEDS = sowing_seeds(sowing)
        SEEDS = SEEDS - sowing

    if MONTH == 4 or MONTH == 10:
        SEEDS = bad_harvest(new_SEEDS)

    result_distribution = distribution_seeds(SEEDS, POPULATION, DISTEMPER, ARMY, ARMY_DISTEMPER)
    SEEDS = result_distribution[0]
    POPULATION = result_distribution[1]
    DISTEMPER = result_distribution[2]
    ARMY = result_distribution[3]
    ARMY_DISTEMPER = result_distribution[4]

    if MONTH % 2 == 0:
        start_war()

    if MONTH % 4 == 0:
        answer2 = str(input('Хотите освоить новые территории?\n1)Да\n2)Нет\n')) #что не работает, если найдёте ошибку буду благодарен (Саша)
        if answer2 == 1 or answer2.lower() == 'да':
            results_conquest = conquest_territory()
            MONEY = MONEY - results_conquest[0]
            SEEDS = SEEDS - results_conquest[1]
    if not(MONTH == 3 and YEAR == 1) and MONTH % 4 == 3:
        TERRITORY = TERRITORY + results_conquest[2]
        POPULATION = POPULATION + results_conquest[3]
        SEEDS = SEEDS + results_conquest[4]

    if MONTH % 3 == 0:
        enlarge_army()

    new_MONEY = taxes_and_pay(POPULATION, ARMY)

    MONEY = MONEY + new_MONEY

    if MONTH == 12:
        MONTH = 0
        YEAR = YEAR + 1
    MONTH = MONTH + 1


print("Условия продолжения игры не выполнены. Ваша страна загнивает. Вы проиграли...")
print('\n\nНарод: {}\nКазна: {}\nЗерно: {}\nСмута: {}\nЗемля: {}\nАрмия: {}\nСмута в армии: {}\nМесяц: {}\n'
          'Год: {}\n'.format(POPULATION, MONEY, SEEDS, DISTEMPER, TERRITORY, ARMY, ARMY_DISTEMPER, MONTH, YEAR))

# TODO: считывание

# TODO: операции
