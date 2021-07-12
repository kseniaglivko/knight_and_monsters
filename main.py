"""
Тестовая игра "Рыцарь и чудовища".

Игрок - рыцарь в фантастической стране.

Задача - победить 10 чудовищ чтобы спасти королевство от нападения и тем самым выиграть игру.
"""


from random import randint, choice
from time import sleep


monster_counter = 0
hp = 15
attack = 10


def game() -> None:
    """Главная функция, запускающая игру и выбирающая то, что произойдет с героем, из всех возможных вариантов."""
    global monster_counter
    if monster_counter == 10:
        print("ПОБЕДА! Вы спасли королевство от нападения чудовищ! :)")
        quit()
    else:
        random_action_selector = [attacking_monsters, eating_apple, finding_sword]
        random_function = choice(random_action_selector)
        random_function()


def attacking_monsters() -> None:
    """Функция, активирующая процесс боя с монстром."""
    monster_hp = randint(5, 35)
    monster_attack = randint(4, 20)
    print(
        f"Начинается БОЙ! "
        f"Вы встретили чудовище с {monster_hp} жизнями и с силой удара {monster_attack}."
        "\nВведите 1, чтобы атаковать чудовище, 2 - чтобы убежать и восстановить силы."
    )
    gamer_reaction_to_monster(hp, monster_hp, monster_attack)


def gamer_reaction_to_monster(hp: int, monster_hp: int, monster_attack: int) -> None:
    """Функция, с помощью которой непосредственно реализуется бой с монстром."""
    global attack
    global monster_counter
    reaction = input()
    if reaction == "1":
        print("Атака!")
        sleep(0.5)
        updated_hp = hp - monster_attack
        updated_monster_hp = monster_hp - attack
        if updated_hp <= 0:
            print("ПОРАЖЕНИЕ! Вы умерли :(")
            quit()
        elif updated_monster_hp <= 0:
            print(
                "Вы победили чудовище! Отдохнув и восстановив силы, вы идете дальше..."
            )
            monster_counter += 1
            print(f"Количество побежденных чудовищ: {monster_counter}. Вы молодец!")
            sleep(2)
            game()
        else:
            print(
                f"Количество ваших жизней: {updated_hp}, количество жизней чудовища: {updated_monster_hp}."
                "\nВведите 1, чтобы атаковать чудовище, 2 - чтобы убежать и восстановить силы."
            )
            gamer_reaction_to_monster(updated_hp, updated_monster_hp, monster_attack)
    elif reaction == "2":
        print("Побег! Вы отдыхаете, восстанавливаете силы и двигаетесь дальше...")
        sleep(2)
        game()
    else:
        print(
            "Некорректный ввод! Введите 1, чтобы атаковать чудовище, 2 - чтобы убежать и восстановить силы."
        )
        gamer_reaction_to_monster(hp, monster_hp, monster_attack)


def eating_apple() -> None:
    """Функция, отвечающая за процесс поедания яблочка, восстанавливающего здоровье."""
    global hp
    apple = randint(1, 2)
    print(
        f"Вы нашли целительное яблочко! Количество жизней, которое оно вам подарит - {apple}."
    )
    hp += apple
    print(
        f"Теперь ваше количество жизней - {hp}. Интересно, что нам встретится дальше на пути?..."
    )
    sleep(2)
    game()


def finding_sword() -> None:
    """Функция, запускающая процесс возможности героя взять меч или отказаться от него."""
    global attack
    sword = randint(11, 20)
    print(
        f"Вы нашли МЕЧ! "
        f"Сила нового меча - {sword}, а сила вашего меча - {attack}."
        "\nВведите 1, чтобы взять новый меч и выкинуть старый, 2 - чтобы пройти мимо."
    )
    gamer_reaction_to_sword(sword)


def gamer_reaction_to_sword(sword: int) -> None:
    """Функция, с помощью которой герой может непосредственно взять меч или пройти мимо."""
    global attack
    reaction = input()
    if reaction == "1":
        attack = sword
        print(
            f"Теперь у вас новый классный меч! Сила вашей атаки - {attack}! Двигаемся дальше..."
        )
        sleep(1.5)
        game()
    elif reaction == "2":
        print("Вы прошли мимо меча. Ну и ладно! Идем дальше...")
        sleep(1.5)
        game()
    else:
        print(
            "Некорректный ввод! Введите 1, чтобы взять новый меч и выкинуть старый, 2 - чтобы пройти мимо."
        )
        gamer_reaction_to_sword(sword)


if __name__ == "__main__":
    """Запуск игры."""
    print(
        'Добро пожаловать в игру "Рыцарь и чудовища"!'
        "\nВам предстоит спасти королевство от нападения 10 чудовищ."
        "\nКоличество ваших жизней - 15, а сила вашей атаки - 10."
        "\nУдачи!"
    )
    game()
