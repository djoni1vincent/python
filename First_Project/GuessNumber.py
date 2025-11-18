
# Угадай число програма
# Пользователь должен угадать число от 1 до 100
# 1. Импортируем необходимые модули

import random

# 2. Генерируем случайное число от 1 до 100

randomNumber = (random.randint(1, 100));
#print (randomNumber)


#3. пользователь вводит число от 1 до 100
while randomNumber: 

    inputPlayer = input("""Guess a number from 1 to 100
                        : """)
    if inputPlayer == "":
        print('type a number')
        continue
    inputPlayerInt = int(inputPlayer)

    print(inputPlayer)

    #4. програма сравнивает ответы, и пишет угадал ли ты или нет, и пишет больше или меньше

    if randomNumber == inputPlayerInt: 
        print ("You win!!! ")
        break
    elif randomNumber > inputPlayerInt:
        print ("Number is higher! ")
    else:
        print ("Number is lover!! ")