T = int(input())
stack = []
for tc in range(T):
    command = input()
    if 'push' in command:
        command, num = command.split()
        stack.append(num)
    elif command == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else :
            print('-1')
    elif command == 'pop':
        if len(stack) != 0:
            a = stack.pop()
            print(a)
        else: print('-1')
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)



