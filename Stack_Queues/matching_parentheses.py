expression = input()

matching = []
for i in range(len(expression)):
    symbol = expression[i]

    if symbol == "(":
        matching.append(i)
    elif symbol == ")":
        left = matching.pop()
        print(expression[left:i +1])