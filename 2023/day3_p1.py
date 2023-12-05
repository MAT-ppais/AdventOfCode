file = open("inputs/day3.txt", "r")
lines = file.readlines()

MAX_CHARS = 140
MAX_LINES = 140

def isValid(number, row, column):
    # print(number)
    column -= 1
    if row > 0 and column < (MAX_CHARS - 1):
        if lines[row - 1][column] != "." or lines[row - 1][column + 1] != ".":
            return True
    if column < (MAX_CHARS - 1):
        if lines[row][column + 1] != ".":
            return True
    if row < (MAX_LINES - 1) and column < (MAX_CHARS - 1):
        if lines[row + 1][column] != "." or lines[row + 1][column + 1] != ".":
            return True
    # print(column)
    if len(number) > 2:
        for i in range(column - 1, (column - len(number)), -1):
            if row > 0:
                if lines[row - 1][i] != ".":
                    return True
            if row < (MAX_LINES - 1):
                if lines[row + 1][i] != ".":
                    return True
    else:
        i = column - len(number) + 1

    if row > 0:
        if lines[row - 1][i] != ".":
            return True
    if row > 0 and i > 0:
        if lines[row - 1][i - 1] != ".":
            return True
    if i > 0:
        if lines[row][i - 1] != ".":
            return True
    if row < (MAX_LINES - 1) and i > 0:
        if lines[row + 1][i - 1] != ".":
            return True
    if row < (MAX_LINES -1) and i > 0:
        if lines[row + 1][i] != ".":
            return True
    return False


def findNumbers(line, lineNr, count):
    number = ""
    location = list()
    line_numbers = list()
    first = True
    lineCount = 0
    for charNr, char in enumerate(line):
        if char.isnumeric():
            number += char
        else:
            if number != "":
                if isValid(number, lineNr, charNr):
                    line_numbers.append(int(number))
                    lineCount += int(number)
                number = ""
    print(line_numbers)
    return lineCount
def main():
    count = 0
    for lineNr, line in enumerate(lines):
        count += findNumbers(line, lineNr, count)
    print(count)

if __name__ == "__main__":
    main()
