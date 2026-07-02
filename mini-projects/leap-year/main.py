#Пошаговый алгоритм:

# Проверьте делимость на 4: Если год не делится на 4, он невисокосный.
# Проверьте делимость на 100: Если год делится на 4, проверьте, делится ли он на 100. Если делится, переходите к шагу 3. Если нет, это високосный год.
# Проверьте делимость на 400: Если год делится на 100, проверьте, делится ли он на 400. Если делится, то это високосный год. Если нет, то это невисокосный год. 

years = [2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2100, 2200]

for year in years:
    
    if year % 400 == 0:
        print(f"{year} - высокосный год")
    elif year % 100 == 0:
        print(f"{year} - ne высокосный год")
    elif year % 4 == 0:
        print(f"{year} - высокосный год")
    else:
        print(f"{year} - ne высокосный год")
        
    
while True:        
    try:
        user_input = (input("Write a year: "))
    except KeyboardInterrupt:
        print(" \ngoodbye")
    
    if user_input == "":
        print("\rwrite a year!! with numbers!!")
        continue
    if int(user_input) % 400 == 0:
        print(f"{user_input} - высокосный год")
    elif int(user_input) % 100 == 0:
        print(f"{user_input} - ne высокосный год")
    elif int(user_input) % 4 == 0:
        print(f"{user_input} - высокосный год")
    else:
        print(f"{user_input} - ne высокосный год")
        
   