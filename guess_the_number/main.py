# программа загадывает число от 1 до 100, а пользователь должен его угадать

import random

number = random.randint(1, 100)  # выбираем случайное число от одного до ста
guess = None  # сюда будет записываться число, которое введет пользователь

print("Я загадал число от 1 до 100. Попробуй угадать!")

# запускаем цикл до тех пор, пока не угадает
while guess != number:
    guess = int(input("Каков будет твой ответ? "))

    if guess < number:
        print("Неверно, загаданное число больше. Попробуй еще раз")
    elif guess > number:
        print("Неверно, загаданное число меньше. Давай еще")
    else:
        print("Бинго!")
