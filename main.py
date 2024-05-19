import os
import time
import random

TEXT_GAME_RULES = """Правила игры:
Истрочекие даты перемешиваются 
тебе нужно запомнить их последовательность
и повторить  после нажатия Enter
"""

current_level = 1
max_number_of_levels = 5
score_user = 0

print(TEXT_GAME_RULES)

historical_events = {
    1492: "Открытие Америки Колумбом",
    1945: "Конец Второй мировой войны",
    1914: "Начало Первой мировой войны",
    1969: "Первый человек на Луне",
    1989: "Падение Берлинской стены",
    2001: "Теракты 11 сентября в США"
}

historical_years = list(historical_events.keys())

while current_level <= max_number_of_levels:
    input("Нажми Enter чтобы продолжить")
    print(f"Текущий уровень: {current_level}")

    random.shuffle(historical_years)
    for i in range(current_level + 1):
        print(historical_years[i])

    time.sleep(4)
    os.system("cls")  # clear

    correct_sequence = True
    for i in range(current_level + 1):

        user_answer = input(f"Введи дату кототорая была {i + 1}: ")
        while not user_answer.isdigit():
            print("введите цифру а не букву")
            user_answer = input(f"Введи дату кототорая была {i + 1}: ")
        user_answer = int(user_answer)

        if user_answer == historical_years[i]:
            print("+")
        else:
            correct_sequence = False
            print(":(")
            break
    if correct_sequence:
        print("Ты смог назвать всю последовательность")
        score_user += current_level

    current_level += 1

print(f"Набрано очков {score_user}")
