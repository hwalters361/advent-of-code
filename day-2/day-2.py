def format(line):
    first_col, second_col = line.split(' ')
    first_norm = ord(first_col.strip()) - 65
    second_norm = ord(second_col.strip()) - 88
    return first_norm, second_norm

def main():
    p1_score = 0
    p2_score = 0
    points = [0,3,6] # loss tie win
    for line in open('day-2.txt', 'r'):
        # Part 1
        elf, me = format(line)
        p1_score += points[((me - elf) + 1) % 3] + (me + 1)
        # Part 2
        elf, result = format(line)
        me = (result - 1 + elf) % 3
        p2_score += points[result] + (me + 1)
    print(p1_score)
    print(p2_score)

if __name__ == "__main__":
    main()