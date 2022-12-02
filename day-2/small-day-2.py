def main():
    print(sum([[0,3,6] [(((ord(line.split(" ")[1].strip()) - 88) - (ord(line.split(" ")[0].strip())-65)) + 1) % 3] + ((ord(line.split(" ")[1].strip()) - 88) + 1) for line in open('day-2.txt', 'r')]))
    print(sum([[0,3,6] [(ord(line.split(" ")[1].strip()) - 88)] + ((((ord(line.split(" ")[1].strip()) - 88) - 1 + (ord(line.split(" ")[0].strip())-65)) % 3) + 1) for line in open('day-2.txt', 'r')]))

if __name__ == "__main__":
    main()