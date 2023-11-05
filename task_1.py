def task_1(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return not stack

print(task_1("()")) 
print(task_1("()[]{}"))
print(task_1("(]"))
