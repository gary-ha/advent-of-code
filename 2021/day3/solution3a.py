def main():
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
        print(lines)

    width = len(lines[0])
    counter = width * [0]
    for num in lines:
        for i, value in enumerate(num):
            if value == '1':
                counter[i] += 1
    gamma = ""
    epsilon = ""
    middle = len(lines) // 2
    for i in counter:
        if i > middle:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(int(gamma, 2) * int(epsilon, 2))

    
if '__main__' == __name__:
    main()