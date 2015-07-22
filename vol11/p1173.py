
# solve function
def solve(line):
    stack = []

    for i in range(len(line)):
        if line[i] == '(' or line[i] == '[':
            stack.append(line[i])
        elif len(stack) > 0:
            if line[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif line[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif line[i] == ']' or line[i] == ')':
                return 'no'
        elif line[i] == ']' or line[i] == ')':
            return 'no'

    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'



# main function
if __name__ == '__main__':
    while True:
        line = input()

        if line == ".":
            break

        result = solve(line)
        print(result)
