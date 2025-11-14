
# Угадай число програма
# Пользователь должен угадать число от 1 до 100
# 1. Импортируем необходимые модули

import random

# 2. Генерируем случайное число от 1 до 100

randomNumber = (random.randint(1, 100));
print (randomNumber)


#3. пользователь вводит число от 1 до 100

inputPlayer = input("Write a number from 1 to 100 ")
inputPlayerInt = int(inputPlayer)

print(inputPlayer)

#4. програма сравнивает ответы, и пишет угадал ли ты или нет, и пишет больше или меньше

if randomNumber == inputPlayerInt: 
    print ("You win! ")
elif randomNumber > inputPlayerInt:
    print ("Number is higher! ")
else:
    print ("Number is lover!! ")