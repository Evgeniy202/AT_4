def task_7(s):
    stack = [-1]
    max_length = 0
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length


print(task_7("(()")) 
print(task_7(")()())")) 
print(task_7(""))  
