def task_6(tokens):
    stack = []
    operators = set(["+", "-", "*", "/"])
    
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            
            if token == "+":
                stack.append(num1 + num2)
            elif token == "-":
                stack.append(num1 - num2)
            elif token == "*":
                stack.append(num1 * num2)
            elif token == "/":
                stack.append(int(num1 / num2))
    
    return stack[0]


print(task_6(["2", "1", "+", "3", "*"]))  
print(task_6(["4", "13", "5", "/", "+"])) 
print(task_6(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) 
