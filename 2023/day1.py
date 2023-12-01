def numbers_string_to_int(number):
    if number == numbers_string[0]: return "1"
    elif number == numbers_string[1]: return "2"
    elif number == numbers_string[2]: return "3"
    elif number == numbers_string[3]: return "4"
    elif number == numbers_string[4]: return "5"
    elif number == numbers_string[5]: return "6"
    elif number == numbers_string[6]: return "7"
    elif number == numbers_string[7]: return "8"
    elif number == numbers_string[8]: return "9"

def look_string_numbers(line, lineNumber, lineIndexIni, lineIndexFin):
    currentIndexMin = 128
    currentIndexMax = -1
    lineNumberIni = int(lineNumber[0])
    lineNumberFin = int(lineNumber[1])
    for number in numbers_string:
        index = line.find(number)
        while index != -1:
            if index < lineIndexIni and index < currentIndexMin:
                numbers_found.append((index, number))
                lineNumberIni = int(numbers_string_to_int(number))
                currentIndexMin = index
            if index > lineIndexFin and index > currentIndexMax:
                lineNumberFin = int(numbers_string_to_int(number))
                currentIndexMax = index
            index = line.find(number, index + 1)
    return str(lineNumberIni) + str(lineNumberFin)

file = open("adventofcode.com_2023_day_1_input.txt", "r")
lines = file.readlines()
numbers = list()
numbers_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
string_list = list()

for count_list, line in enumerate(lines):
    lineDigits = 0;
    lineNumber = ""
    currentDigit = ""
    numbers_found = list()
    string_value = ""
    lineIndexIni = 128
    lineIndexFin = -1
    for i in range(len(line)):
        if line[i].isdigit():
            currentDigit = line[i]
            lineIndexFin = i
            if lineDigits == 0:
                lineIndexIni = i
                lineDigits +=1
                lineNumber += line[i]
    lineNumber += currentDigit
    string_value = look_string_numbers(line, lineNumber, lineIndexIni, lineIndexFin)
    numbers.append(int(string_value))

counter = 0
for i in range(len(numbers)):
    counter += numbers[i]
print(counter)
