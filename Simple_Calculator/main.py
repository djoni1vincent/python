# Калькулятор
# 1.Пользователь вводит 2 числа 

askPlusOrMinus = input("What you want to choose:  "
"write 1 or 2 " \
"+ " \
"- ")

if askPlusOrMinus == "1":
    firstNum = input("Write first number ")
    secondNum = input("Write another n1umber ")
    intOne = int(firstNum)
    intTwo = int(secondNum)
 
    calculate = intOne + intTwo
    print(f"if we {firstNum} + {secondNum} we get {calculate}")

if askPlusOrMinus == "2":
    firstNum = input("Write first number ")
    secondNum = input("Write another number ")
    intOne = int(firstNum)
    intTwo = int(secondNum)
    
    calculate = intOne - intTwo
    print(f"if we {firstNum} - {secondNum} we get {calculate}")


else:
    print("Wrong input (choose 1 or 2)")