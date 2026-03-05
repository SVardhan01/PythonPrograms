s = "{[()]}"
stack = []
for ch in s:
    if ch =='[' or ch == '(' or ch == '{':
        stack.append(ch)
    else:
        if not stack:
            print("invalid")
            break
        top = stack.pop()
        if (ch == ']' and top !='[') or (ch == ')' and top !='(') or (ch == '}' and top !='{'):
            print("invalid")
            break
else:    
    if not stack:
        print("Valid")
    else:
        print("invalid")