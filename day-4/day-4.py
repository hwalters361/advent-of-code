def priority(str):
    p = 0
    if str.isupper():
        p += 26
    p+=ord(str.lower()) - 96
    return p

def main():
    sum1 = 0
    sum2 = 0
    for line in open('day-4.txt', 'r'):
        first, second = line.split(",")
        pair1 = list(map(int, first.strip().split("-")))
        pair2 = list(map(int, second.strip().split("-")))
        if min(pair1) >= min(pair2) and min(pair1) <= max(pair2):
            if max(pair1) <= max(pair2):
                sum1+=1
            sum2+=1
        elif min(pair2) >= min(pair1) and min(pair2) <= max(pair1):
            if max(pair2) <= max(pair1):
                sum1+=1
            sum2+=1

    print(sum1)
    print(sum2)

if __name__ == "__main__":
    main()