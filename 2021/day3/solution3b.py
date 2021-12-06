def main():
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
        print(lines)

    width = len(lines[0])

    oxygen_lines = lines
    co2_lines = lines
    oxygen = ""
    co2 = ""
    for i in range(width):
        oxygen_lines = calculate(oxygen_lines, i, True)
        co2_lines = calculate(co2_lines, i, False)
        if len(oxygen_lines) == 1:
            oxygen = oxygen_lines[0]
        if len(co2_lines) == 1:
            co2 = co2_lines[0]

    print(int(oxygen, 2) * int(co2, 2))


def calculate(lines, index, bool):
    totals = {0: [], 1: []}
    for line in lines:
        if line[index] == "1":
            totals[1].append(line)
        else:
            totals[0].append(line)
    if (len(totals[1]) > len(totals[0]) and bool) or (len(totals[1]) < len(totals[0]) and not bool) or \
            (len(totals[1]) == len(totals[0]) and bool):
        return totals[1]
    else:
        return totals[0]


if '__main__' == __name__:
    main()