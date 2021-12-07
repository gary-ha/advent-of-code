class Board:
    def __init__(self, chunks):
        self.rows = [set(i) for i in chunks]
        self.columns = [set(i) for i in zip(*chunks)]

    def find(self, number):
        empty = set()
        for i in self.rows:
            i.discard(number)
        for i in self.columns:
            i.discard(number)
        if empty in self.rows or empty in self.columns:
            return True

    def non_found(self):
        total = 0
        for row in self.rows:
            for num in row:
                total += num
        return total


def main():
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    numbers = [int(i) for i in lines[0].split(",")]
    rows = [[int(n) for n in line.split()] for line in lines[1:]]

    chunks = []
    templater = []
    for line in rows:
        if line:
            templater.append(line)
        if len(templater) == 5:
            chunks.append(templater)
            templater = []

    boards = [Board(chunk) for chunk in chunks]

    for num in numbers:
        for board in boards:
            if board.find(num):
                print(board.non_found() * num)
                return


if '__main__' == __name__:
    main()
