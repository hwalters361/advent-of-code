from collections import deque

def break_four(line):
    return [line[i:i+4] for i in range(0, len(line), 4)]

def main():
    """Used a deque for part 1 and a python list for part 2"""
    stacks1 = [deque() for x in range(9)]
    stacks2 = [[] for x in range(9)]
    lines = []
    for line in open('day-5.txt'):
        if len(stacks1[0]) < 8:
            carts = break_four(line)
            for i in range(9):
                if carts[i].strip() != '':
                    stacks1[i].append(carts[i].strip())
                    stacks2[i].append(carts[i].strip())
    for line in open('day-5.txt'):
        instruction = line.split(" ")
        if instruction[0] == "move":
            num_carts = int(instruction[1])
            origin = int(instruction[3])-1
            destination = int(instruction[5])-1
            # for part 1
            for i in range(num_carts):
                cart = stacks1[origin].popleft()
                stacks1[destination].appendleft(cart)
            # for part 2
            stacks2[destination] = stacks2[origin][:num_carts] + stacks2[destination]
            stacks2[origin] = stacks2[origin][num_carts:]


    output1 = ''.join([stacks1[i][0][1] for i in range(len(stacks1))])
    output2 = ''.join([stacks2[i][0][1] for i in range(len(stacks2))])
    print(output1)
    print(output2)
if __name__ == "__main__":
    main()