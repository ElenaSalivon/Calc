def calc(action, arg1, arg2=0):
    match action:
        case "+":
            return arg1 + arg2
        case "-":
            return arg1 - arg2
        case "*":
            return arg1 * arg2
        case "/":
            if arg2 != 0:
                return arg1 / arg2
            else:
                return "Division by ZERO"
        case "%":
            if arg2 != 0:
                return arg1 % arg2
            else:
                return "Division by ZERO"
        case "sin":
            return math.sin(arg1)
        case "cos":
            return math.cos(arg1)
#space for calc


#action for the body for Alpher

act = ""
while act != "x":
    act = input("Choose action + - * / % sin cos (for exit - x): ")
    if act == "sin" or act == "cos":
        arg1 = int(input("\t Input X: "))
        print("Result is:", calc(act, arg1))
    elif act == "+" or act == "-" or act == "*" or act == "/" or act == "%":
        arg1 = int(input("\t Input X: "))
        arg2 = int(input("\t Input Y: "))
        print("Result is:", calc(act, arg1, arg2))
    else:
        print("\tWrong choise!")

#smth wrong