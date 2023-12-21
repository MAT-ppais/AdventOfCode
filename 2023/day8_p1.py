def convert_to_map(lines):
    map = list()
    instructions = lines[0].strip()
    for idx, line in enumerate(lines):
        if idx != 0 and idx != 1:
            map.append((line.split("=")[0].strip(), (line.split("=")[1].strip().split(",")[0][1:], line.split("=")[1].strip().split(",")[1].strip(")").replace(" ", ""))))
    return instructions, map

def check_next(instruction, map, current_pos, count):
    if instruction == 'L':
        for idx, map_i in enumerate(map):
            if map_i[0] == current_pos[1][0]:
                current_pos = map[idx]
                return current_pos
    elif instruction == 'R':
        for idx, map_i in enumerate(map):
            if map_i[0] == current_pos[1][1]:
                current_pos = map[idx]
                return current_pos

def main():
    with open("2023/inputs/day8.txt") as file:
        lines = file.readlines()
    instructions, map = convert_to_map(lines)
    for i in range(len(map)):
        if map[i][0] == "AAA":
            current_pos = map[i]
    found = False
    count = 0
    while not found:
        for instruction in instructions:
            current_pos = check_next(instruction, map, current_pos, count)
            count += 1
            if current_pos[0] == "ZZZ":
                found = True
                break
    print(count)



if __name__ == "__main__":
    main()
