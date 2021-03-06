def main():
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
        print(lines)

    horizontal = depth = 0
    for i in lines:
        split_list = i.split()
        if split_list[0] == "forward":
            horizontal += int(split_list[1])
        if split_list[0] == "down":
            depth += int(split_list[1])
        if split_list[0] == "up":
            depth -= int(split_list[1])

    print(horizontal * depth)


if '__main__' == __name__:
    main()
