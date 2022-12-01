def main():
    temp_sum = 0
    top_3 = [0,0,0]
    for line in open('day-1.txt', 'r'):
        if line == "\n":
            if min(top_3) < temp_sum:
                top_3.remove(min(top_3))
                top_3.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum += int(line)
    # Part 1 answer output (Expected 69626)
    print(f'Max cals: {top_3[0]}')
    # Part 2 answer output (Expected 206780)
    print(f'Sum top 3: {sum(top_3)}')

if __name__ == "__main__":
    main()