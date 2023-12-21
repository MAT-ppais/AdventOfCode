import math

global_count = 0

def verify_combination(string, combination):
    global global_count
    verify_count = 0
    combination_list = list()
    for idx, char in enumerate(string):
        if char == '#':
            verify_count += 1
        else:
            if verify_count != 0:
                combination_list.append(str(verify_count))
                verify_count = 0
    if verify_count != 0:
        combination_list.append(str(verify_count))
    if combination_list == combination:
        global_count += 1


def count_combinations(input_tuple):
    original_string, combination = input_tuple
    interrogants = [i for i, char in enumerate(original_string) if char == '?']
    num_interrogants = len(interrogants)

    for binary in range(2 ** num_interrogants):
        modified_string = list(original_string)
        binary_str = format(binary, f'0{num_interrogants}b')

        for i in range(num_interrogants):
            if binary_str[i] == '1':
                replacement = '#'
            else:
                replacement = '.'
            modified_string[interrogants[i]] = replacement

        modified_string = ''.join(modified_string)
        verify_combination(modified_string, combination)


def main():
    with open("inputs/day12.txt") as file:
        lines = file.readlines()
    tuples = list()
    for idx, line in enumerate(lines):
        splittedLine = line.strip().split(" ")
        numbers = splittedLine[1].strip().split(",")
        tuples.append((splittedLine[0], numbers))
    for tuple in tuples:
        count_combinations(tuple)
    print(global_count)


if __name__ == "__main__":
    main()



