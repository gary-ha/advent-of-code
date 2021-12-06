def main():
    with open('input.txt') as f:
        lines = [int(line.rstrip('\n')) for line in f]
        print(lines)

    new_list = []
    for i in range(len(lines) - 2):
        new_list.append(sum(lines[i:i+3]))
    print(new_list)

    increased = 0
    for i in range(1, len(new_list)):
        if new_list[i] > new_list[i-1]:
            increased += 1
    print(increased)


if '__main__' == __name__:
    main()
