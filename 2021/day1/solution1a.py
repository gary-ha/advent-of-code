def main():
    with open('input.txt') as f:
        lines = [int(line.rstrip('\n')) for line in f]

    increased = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i-1]:
            increased += 1
    print(increased)


if '__main__' == __name__:
    main()