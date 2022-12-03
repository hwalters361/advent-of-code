def priority(str):
    p = 0
    if str.isupper():
        p += 26
    p+=ord(str.lower()) - 96
    return p

def main():
    sum1 = 0
    sum2 = 0
    three_set = []
    for line in open('day-3.txt', 'r'):
        half1 = line[:int(len(line)/2)].strip()
        half2 = line[int(len(line)/2):].strip()
        for i in half1:
            if i in half2:
                sum1+=priority(i)
                break
    
    for line in open('day-3.txt', 'r'):
        line = line.strip()
        if len(three_set) < 3:
            three_set.append(line)
            if len(three_set) == 3:
                for i in max(three_set):
                    if (i in three_set[0]) and (i in three_set[1]) and (i in three_set[2]):
                        sum2+=priority(i)
                        break
                three_set = []
    print(sum1)
    print(sum2)

if __name__ == "__main__":
    main()