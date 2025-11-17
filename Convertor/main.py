# 1. Програма которая переводит килограмы в грамы
# 2. Информацию берет от пользователя из input
# 3. Потом конвертирует значение с килограм в грам
# 
#
#


# userInput =  int(input('Write grams '))
# result = kg = userInput / 1000
# print(f"If we converted  {userInput} gr, we get {result} kg ")


def kgToGrams(grams):
    return grams * 1000
inputKg = int(input("Write Kilograms "))
result = kgToGrams(inputKg)
print(f"converted {inputKg}kg to {result} ")