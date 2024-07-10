# def perform_operation(num1, num2, operation):
#     match operation:
#         case "add":
#             result = num1+num2
#             return result
#         case "subtract" :
#             result = num1 - num2
#         case "multiply":
#             result  = num1 * num2
#             return result
#         case "divide":
#             if num2 == 0:
#                 result ="invalid operation"
#             else :
#                 result = num1/num2
#             return result
#         case _:
#             return print("invalid symbol")
def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
     
