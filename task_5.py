def task_5(s):
    stack = []
    curr_num = 0
    curr_str = ''

    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append((curr_str, curr_num))
            curr_str = ''
            curr_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += char

    return curr_str


print(task_5("3[a]2[bc]")) 
print(task_5("3[a2[c]]")) 
print(task_5("2[abc]3[cd]ef"))
