def perform_operation (num1: float, num2: float, operation: str):
    if operation == "add":
        result = num1 + num2
        return result
    elif operation == "subtract":
        result = num1- num2
        return result
    elif operation == "multiply":
        result = num1 * num2
        return result
    elif operation == "divide":
        if num2 == 0:
            print ("division by zero is not allowed")
        else:
            result = num1 / num2
            return result