while True:
    
    expression = input("calculate or write 'e' to exit\n ")
    if expression == "e":
        break
    
    def parse_expression(expression):
        i = expression.split()
        a, oper, b = i[0], i[1], i[2]
        number1 = int(a)
        number2 = int(b)
        return (number1, oper ,number2)

    number1, oper, number2 = parse_expression(expression)

    def calculate(number1, oper, number2):
        if oper == "+":
            return number1 + number2
        elif oper == "-":
            return number1 - number2
        elif oper == "/":
            return number1 // number2
        elif oper == "*":
            return number1 * number2
          
        
    result = calculate(number1, oper, number2)

        
    print(f"Your result is: {result}")
    
  

