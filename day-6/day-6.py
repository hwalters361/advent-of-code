def check_file(filename, max_length):
    unique_chars = []
    itr = 1
    with open(filename, 'r') as f:
        while True:
            # Read from file
            c = f.read(1)
            if not c:
                break
            if c in unique_chars:
                repeat_index = unique_chars.index(c)
                unique_chars = unique_chars[repeat_index+1:] + [c]
            elif c not in unique_chars:
                unique_chars.append(c)
            if len(unique_chars) == max_length:
                break
            else:
                itr+=1
    return itr

def main():
    itr1 = check_file('day-6.txt', 4)
    itr2 = check_file('day-6.txt', 14)
    print(itr1)
    print(itr2)


        

if __name__ == "__main__":
    main()