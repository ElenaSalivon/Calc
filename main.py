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