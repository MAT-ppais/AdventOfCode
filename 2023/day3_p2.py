file = open("2023/inputs/day3.txt", "r")
lines = file.readlines()
global_list = list()

# will contain (char_row, char_col, n1, n2)
gears_list = list()

MAX_CHARS = 140
MAX_LINES = 140

def add_to_gear_list(char_row, char_col, num):
    alreadyExists = False
    for i in range(len(gears_list)):
        if gears_list[i][0] == char_row and gears_list[i][1] == char_col:
            gears_list[i] = (gears_list[i][0], gears_list[i][1], gears_list[i][2], num)
            alreadyExists = True
    if alreadyExists is False:
        gears_list.append((char_row, char_col, num, None))

def findMultiply(number, row, column):
    column -= 1
    if row > 0:
        if lines[row - 1][column] == "*":
            add_to_gear_list(row-1, column, number)
            return
    if column < (MAX_CHARS - 1):
        if lines[row - 1][column + 1] == "*":
            add_to_gear_list(row-1, column+1, number)
            return
    if column < (MAX_CHARS - 1):
        if lines[row][column + 1] == "*":
            add_to_gear_list(row, column+1, number)
            return
    if row < (MAX_LINES - 1):
        if lines[row + 1][column] == "*":
            add_to_gear_list(row+1,column,number)
            return
    if row < (MAX_LINES - 1) and column < (MAX_CHARS - 1):
        if lines[row + 1][column + 1] == "*":
            add_to_gear_list(row+1,column+1,number)
            return
    if len(number) > 2:
        for i in range(column - 1, (column - len(number)), -1):
            if row > 0:
                if lines[row - 1][i] == "*":
                    add_to_gear_list(row-1,i,number)
                    return
            if row < (MAX_LINES - 1):
                if lines[row + 1][i] == "*":
                    add_to_gear_list(row+1,i,number)
                    return
    else:
        i = column - len(number) + 1

    if row > 0:
        if lines[row - 1][i] == "*":
            add_to_gear_list(row-1, i, number)
            return
    if row > 0 and i > 0:
        if lines[row - 1][i - 1] == "*":
            add_to_gear_list(row-1, i-1, number)
            return
    if i > 0:
        if lines[row][i - 1] == "*":
            add_to_gear_list(row, i-1, number)
            return
    if row < (MAX_LINES - 1) and i > 0:
        if lines[row + 1][i - 1] == "*":
            add_to_gear_list(row+1, i-1, number)
            return
    if row < (MAX_LINES -1) and i > 0:
        if lines[row + 1][i] == "*":
            add_to_gear_list(row+1, i, number)
            return

def isValid(number, row, column):
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


def findNumbers(line, lineNr, count,line_coordenates,multiply_coordenates):
    number = ""
    location = list()
    line_numbers = list()
    multiply_line_list = list()
    first = True
    lineCount = 0
    for charNr, char in enumerate(line):
        if char.isnumeric():
            number += char
        else:
            if number != "":
                if isValid(number, lineNr, charNr):
                    line_numbers.append((int(number), lineNr, charNr))
                    lineCount += int(number)
                findMultiply(number, lineNr, charNr)
                number = ""
    line_coordenates.append(line_numbers)
    multiply_coordenates.append(multiply_line_list)
    return lineCount

def main():
    count = 0
    line_coordenates = list()
    multiply_coordenates = list()
    for lineNr, line in enumerate(lines):
        count += findNumbers(line, lineNr, count, line_coordenates, multiply_coordenates)
    multiply_count = 0
    for gear in gears_list:
        if gear[2] is not None and gear[3] is not None:
            multiply_count += (int(gear[2]) * int(gear[3]))
    print(multiply_count)

if __name__ == "__main__":
    main()
