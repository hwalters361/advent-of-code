def main():
    max_sum = 0
    temp_sum = 0
    for line in open('day-1.txt', 'r'):
        if line == "\n":
            max_sum = temp_sum if (max_sum < temp_sum) else max_sum
            temp_sum = 0
        else:
            temp_sum += int(line)
    print(max_sum)


if __name__ == "__main__":
    main()