if __name__ == '__main__':
    N = int(input())
    list_numbers = []
    for i in range(N):
        commands = input().split()
        if commands[0] == "insert":
            position = int(commands[1])
            number = int(commands[2])
            list_numbers.insert(position, number)
        elif commands[0] == "print":
            print(list_numbers)
        elif commands[0] == "remove":
            number = int(commands[1])
            list_numbers.remove(number)
        elif commands[0] == "append":
            number = int(commands[1])
            list_numbers.append(number)
        elif commands[0] == "sort":
            list_numbers.sort()
        elif commands[0] == "pop":
            list_numbers.pop()
        elif commands[0] == "reverse":
            list_numbers.reverse()
