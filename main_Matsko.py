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
                         "Не хотите ли продать несколько мешков зерна городу N?"] #Сюда можно добавить ещё больше разных текстов, их тут два чисто для примера
    print(trading_countries[random.randint(0, len(trading_countries) - 1)])
    course = random.randint(20, 35)
    print("Вам предлагают обмен по курсу: {} зол./мешок".format(course))
    try:
        seeds_amount = int(input("Сколько мешков продадим?\n"))
    except ValueError:
        seeds_amount = int(input("Введите натуральное число: "))
    if seeds_amount == 0:
          print("Вы отказались торговать. Каждый остался при своём")
    elif seeds_amount != 0 and seeds_amount <= seeds:
          print("Вы продали {} мешков зерна и получили за это {} золота".format(seeds_amount, seeds_amount * course))
          seeds -= seeds_amount
          money += seeds_amount * course
    else:
        print("Вы жулик! У вас ничего не купят в этом месяце.")
    print("У вас {} золота, {} зерна.".format(money, seeds))
    return seeds, money


def buy_seeds(seeds, money):
    course = random.randint(20, 35)
    print("\nЕсть возможность купить зерно у соседнего города по курсу: {} зол./мешок.".format(course))
    try:
        seeds_amount = int(input("Сколько мешков купим?\n"))
    except ValueError:
        seeds_amount = int(input("Введите натуральное число: "))
    if seeds_amount == 0:
        print("Вы отказались торговать. Каждый остался при своём")
    elif seeds_amount != 0 and seeds_amount * course <= money:
        print("Вы купили {} мешков зерна и запатили за это {} золота".format(seeds_amount, seeds_amount * course))
        seeds += seeds_amount
        money -= seeds_amount * course
    else:
        print("Вы не можете залезть в долг! Торговля Отменяется.")
    print("У вас {} золота, {} зерна.".format(money, seeds))
    return seeds, money


def sowing_seeds(num_seeds):            #Функция возвращает прибавку к зерну
    new_seeds = 0
    for i in range(num_seeds):
        new_seeds += random.randint(3, 5)
    return new_seeds


def distribution_seeds(seeds, population0, distemper, army, army_distemper):
    print("\nПора раздавать зерно людям. У вас {} зерна.".format(seeds))
    answer_f1 = int(input("Сколько зерна раздать?\n"))
    recommend = math.ceil((population0 - army) * 0.5) + army
    if answer_f1 < recommend:
        distemper = int((distemper * population0 + (recommend - answer_f1) * 3 / 4) / population0 * 100) / 100
        army_distemper = int((army_distemper * army + (recommend - answer_f1) / 4) / army * 100) / 100
        population1 = int(population0 - int((recommend - answer_f1) / 0.5 * 0.65))
        if population1 < 0:
            population1 = 0
    elif answer_f1 > recommend:
        distemper = int((distemper * population0 + (recommend - answer_f1) * 3 / 4) / population0 * 100) / 100
        if distemper < 0:
            distemper = 0.00
        army_distemper = int((army_distemper * army + (recommend - answer_f1) / 4) / army * 100) / 100
        if army_distemper < 0:
            army_distemper = 0.00
        population1 = int(population0 + (answer_f1 - recommend) / 0.5 * 0.65)
        if population1 > population0 + population0 / 4:
            population1 = int(population0 + population0 * random.randint(23, 27) / 100)
    else:
        population1 = population0
    seeds = seeds - answer_f1
    print("Вы раздали {} мешков зерна народу". format(answer_f1))
    return seeds, population1, distemper, army, army_distemper


def start_war():
    pass


def conquest_territory():
    answer2 = str(input("\nХотите освоить новые территории?\n1)Да\n2)Нет\n"))
    if answer2 == '1' or answer2.lower() == 'да':
        costs = int(random.randint(2000, 4500))
        need_seeds = int(random.randint(40, 100))
        new_territory = int(random.randint(0, 5))
        people = int(random.randint(0, 25) - random.randint(0, 20))
        seeds = int(math.ceil(people * 0.5))
    else:
        costs = 0
        need_seeds = 0
        new_territory = 0
        people = 0
        seeds = 0
    return [costs, need_seeds, new_territory, people, seeds]



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
        new_seeds = int(new_seeds * (random.randint(50, 70)) / 100)
        print("\nВас постиг неурожай")
    print("\nВы собрали {} зерна".format(new_seeds))
    return new_seeds


def attack():
    pass


def many_rats(seeds):
    pass


def revolution():
    pass


def you_ill(month):
    print("Вы заболели. Пропуск хода.")
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
    print("\n\nНарод: {}\nКазна: {}\nЗерно: {}\nСмута: {}\nЗемля: {}\nАрмия: {}\nСмута в армии: {}\nМесяц: {}\n"
          "Год: {}\n".format(POPULATION, MONEY, SEEDS, DISTEMPER, TERRITORY, ARMY, ARMY_DISTEMPER, MONTH, YEAR))

    POPULATION = POPULATION + POPULATION * (random.randint(1, 5)) / 1000 - POPULATION * (random.randint(1, 5)) / 1000

    results_sale = sale_seeds(SEEDS, MONEY)
    SEEDS = results_sale[0]
    MONEY = results_sale[1]

    results_buy = buy_seeds(SEEDS, MONEY)
    SEEDS = results_buy[0]
    MONEY = results_buy[1]

    if MONTH == 1 or MONTH == 6:
        print("\nУ вас {} зерна".format(SEEDS))
        sowing = int(input("Сколько зерна засеять?\n".format(SEEDS)))
        new_SEEDS = sowing_seeds(sowing)
        SEEDS = SEEDS - sowing

    if MONTH == 4 or MONTH == 10:
        SEEDS = bad_harvest(new_SEEDS) + SEEDS

    result_distribution = distribution_seeds(SEEDS, POPULATION, DISTEMPER, ARMY, ARMY_DISTEMPER)
    SEEDS = result_distribution[0]
    POPULATION = result_distribution[1]
    DISTEMPER = result_distribution[2]
    ARMY = result_distribution[3]
    ARMY_DISTEMPER = result_distribution[4]

    if MONTH % 2 == 0:
        start_war()

    if MONTH % 1 == 0:
        result_conquest = conquest_territory()
        MONEY = MONEY - result_conquest[0]
        SEEDS = SEEDS - result_conquest[1]
        TERRITORY = TERRITORY + result_conquest[2]
        POPULATION = POPULATION + result_conquest[3]
        SEEDS = SEEDS + result_conquest[4]
        print("\nНа освоение территорий было потрачено: {} золото, {} зерна."
              "\nВ ходе освоения территории было получено: {} земля, {} народ, {} "
              "зерна.".format(result_conquest[0], result_conquest[1], result_conquest[2], result_conquest[3],
                              result_conquest[4]))

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
