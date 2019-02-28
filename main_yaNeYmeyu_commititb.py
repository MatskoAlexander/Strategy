import random
import math

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


def sale_seeds(seeds, money):
    course = random.randint(20, 35)
    trading_countries = ["Соседняя страна желает купить у вас зерна, ",
                         "Не хотите ли продать несколько мешков зерна городу N?"]
    print(trading_countries[random.randint(0, len(trading_countries) - 1)])
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


def sowing_seeds(num_seeds):
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


def start_war(army):
    voyna = str(input("\nХотите развлечься и развязать войну?\n1)Да\n2)Нет\n"))
    if voyna.lower() == "да" or voyna == "1":
        variaty = random.randint(0, 1)
        conquested_territory = math.ceil(random.randint(3, 6))
        conquest_money = math.ceil(random.randint(5000, 10000))
        conquest_population = math.ceil(random.randint(100, 500))
        killed_army = math.ceil(random.randint(11, 13))
        army = army // (killed_army / 10)
        if variaty == 0:
            print("Вы победили в войне, захватив ", conquested_territory, " земля, ", conquest_money, " золота, ",
                  conquest_population, " людей. Поздравляем!")
            return [conquested_territory, conquest_money, conquest_population, army]
        else:
            conquest_money = -conquest_money
            conquested_territory = -conquested_territory
            conquest_population = -conquest_population
            print("Вы проиграли в войне, потеряв ", -conquested_territory, " земля, ", -conquest_money, " золота, ",
                  -conquest_population, " людей. Бывает.")
            return [conquested_territory, conquest_money, conquest_population, army]
    else:
        print("Такой шанс упускаете.")
        return [0, 0, 0, army]


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


def enlarge_army(army, population):
    print("\nЗакончился призыв, на службу в вашу армию поступило ", POPULATION // 20, " человек")
    army += population // 20
    population -= population // 20
    return army, population


def taxes_and_pay(population, army):
    money = int((population - army) * 10)
    if money < 0:
        money = 0
    pay = army * 12
    total = money - pay
    print("\nВы получили налоги: {} золота. Вы заплатили жалование армии: {} золота. Итого: {} золота".
          format(money, pay, total))
    return total


def bad_harvest(new_seeds):
    rnd = random.randint(1, 15)
    if rnd == 1:
        new_seeds = int(new_seeds * (random.randint(50, 70)) / 100)
        print("\nВас постиг неурожай")
    print("\nВы собрали {} зерна".format(new_seeds))
    return new_seeds


def attack():
    print("На вас напали. Придётся защищать государство от врага")
    enemy_army = ARMY*(random.randint(50, 500)/100)
    win_chance = 0.5
    if enemy_army <= ARMY:
        win_chance += enemy_army/ARMY
        print("Так как ваша армия больше, чем у соперника, шансы на победу увеличиваются(армия соперника составляет всего {}% от вашей".format(math.ceil(enemy_army/ARMY*100))
    else:
        win_chance -+ ARMY/enemy_army/5
        print("Так как ваша армия меньше, чем у соперника, шансы на победу понижаются(армия соперника составляет в {} раз больше вашей".format(math.ceil(enemy_army/ARMY))
    win = random.randint(1, 100)
    new_tactic = int(input("Не хотите ли вы испробовать новую боевую тактику от одного из опытных полководцев? Если она сработает, мы выиграем эту войну абсолютно без потерь(вероятность победы в таком случае будет равняться двадцати процентам). Но если проиграем, то потери будут невосполнимыми"))
    if new_tactic == 1:
        win_chance = 0.2
    else:
        win_chance = 0
    if win_chance*100 <= win:
        print("Ура, вы победили! За победу в войне вам полагается денежное вознаграждение!")
    else:
        print("Кажется, вы проиграли эту войну. Территория и ресурсы страны уменьшились, народ негодует")
    #Саня, разберись сам, сколько надо добавить или убавить, потому что только ты точно знаешь экономическую систему в этом замечательном государстве. И попробуй сделать не точное число, а чтобы оно зависело от размеров армий, нынешнего количества денег.

def many_rats(seeds):
    rnd = random.randint(1, 20)
    if rnd == 1:
        lost_seeds = int(seeds * random.randint(3, 5) / 10)
        seeds = seeds - lost_seeds
        print("\nВ амбарах развелись крысы. Вы потеряли: {} зерно".format(lost_seeds))
    return seeds


def revolution(distemper):
    rnd = random.randint(1, 50)
    if rnd == 1:
        print('\nПроизошло восстание. Смута повысилась')
        distemper = distemper + random.randint(1, 10) / 100
    return distemper


def new_hero(distemper):
    rnd = random.randint(1, 100)
    if rnd == 1:
        distemper = distemper - random.randint(3, 5) / 10
        if distemper <= 0:
            distemper = 0.00
        print("\nВ королевстве появился герой. Народ воспрял духом. Смута понизилась")
    return distemper


def treasure(money):
    rnd = random.randint(1, 20)
    if rnd == 1:
        get_treasure = + random.randint(15000, 30000)
        money = money + get_treasure
        print('\nВы нашли клад: {} золото'.format(get_treasure))
    return money


def epidemy(population, army):
    rnd = random.randint(1, 20)
    if rnd == 1:
        dead_population = int(population - population // 1.5)
        population = population // 1.5
        dead_army = int(army - army // 1.25)
        army = army // 1.25
        print('\nВас настигла эпидемия. Умерло: {} народ, {} армия'.format(dead_population, dead_army))
    return population, army


def refugee(population):
    rnd = random.randint(1, 10)
    if rnd == 1:
        new_people = random.randint(50, 300)
        population = population + new_people
        print("\nК вам прибыло {} беженцы".format(new_people))
    return population


def people_needs(money, distemper):
    needs = ["\nНарод просит у вас денег для покупки новых сельскохозяйственных инструментов.",
             "\nНедавно построенная деревня просит у вас золота для постройки трактира."]
    rnd1 = random.randint(1, len(needs) - 1)
    rnd2 = random.randint(1, 7)
    if rnd2 == 1:
        need_money = random.randint(2000, 5000)
        print(needs[rnd1])
        answerf2 = input("Для этого требуется: {} золота. У вас {} золота. Поможите?\n1)Да\n2)Нет\n".
                         format(need_money, money))
        if answerf2 == 1 or answerf2.lower() == "да" or answerf2 == "1":
            money = money - need_money
            distemper = distemper - random.randint(1, 4) / 100
            if distemper < 0:
                distemper = 0
            print("Вы помогли своему народу потратив {} золота. Смута понизилась".format(need_money))
        else:
            distemper = distemper + random.randint(1, 4) / 100
            print("Вы отказались помогать своему народу. Смута повысилась")
    return money, distemper


# TODO: ситуация

# TODO: вызов функций

print("\nПриветсвуею, правитель! Вы управляете небольшим государством. Вам предстоит решать его судьбу. Дерзайте!")
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
    if POPULATION == 0:
        break

    if MONTH % 4 == 0:
        result_conquest = conquest_territory()
        MONEY = MONEY - result_conquest[0]
        SEEDS = SEEDS - result_conquest[1]
        TERRITORY = TERRITORY + result_conquest[2]
        POPULATION = POPULATION + result_conquest[3]
        SEEDS = SEEDS + result_conquest[4]
        print("\nНа освоение территорий было потрачено: {} золото, {} зерна."
              "\nВ ходе освоения территории было получено: {} земля.".format(result_conquest[0], result_conquest[1],
                                                                             result_conquest[2]))

    if MONTH % 3 == 0:
        results_enlarge = enlarge_army(ARMY, POPULATION)
        ARMY = results_enlarge[0]
        POPULATION = results_enlarge[1]

    POPULATION = refugee(POPULATION)

    if MONTH % 2 == 0:
        results_war = start_war(ARMY)
        TERRITORY = int(TERRITORY + results_war[0])
        MONEY = int(MONEY + results_war[1])
        POPULATION = int(POPULATION + results_war[2])
        ARMY = int(results_war[3])

    new_MONEY = taxes_and_pay(POPULATION, ARMY)
    MONEY = MONEY + new_MONEY

    results_ask = people_needs(MONEY, DISTEMPER)
    MONEY = results_ask[0]
    DISTEMPER = results_ask[1]
    SEEDS = many_rats(SEEDS)
    DISTEMPER = revolution(DISTEMPER)
    DISTEMPER = new_hero(DISTEMPER)
    MONEY = treasure(MONEY)
    results_epidemy = epidemy(POPULATION, ARMY)
    POPULATION = int(results_epidemy[0])
    ARMY = int(results_epidemy[1])

    if MONTH == 12:
        MONTH = 0
        YEAR = YEAR + 1
    MONTH = MONTH + 1


print("Условия продолжения игры не выполнены. Ваша страна загнивает. Вы проиграли...")
print("\n\nНарод: {}\nКазна: {}\nЗерно: {}\nСмута: {}\nЗемля: {}\nАрмия: {}\nСмута в армии: {}\nМесяц: {}\n"
          "Год: {}\n".format(POPULATION, MONEY, SEEDS, DISTEMPER, TERRITORY, ARMY, ARMY_DISTEMPER, MONTH, YEAR))

# TODO: считывание

# TODO: операции
