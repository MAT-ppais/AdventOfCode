def convert_to_map(lines):
    map = list()
    map_dict = dict()
    instructions = lines[0].strip()
    for idx, line in enumerate(lines):
        if idx != 0 and idx != 1:
            map.append((line.split("=")[0].strip(), (line.split("=")[1].strip().split(",")[0][1:], line.split("=")[1].strip().split(",")[1].strip(")").replace(" ", ""))))
            map_dict[line.split("=")[0].strip()] = (line.split("=")[1].strip().split(",")[0][1:], line.split("=")[1].strip().split(",")[1].strip(")").replace(" ", ""))
    return instructions, map_dict

def check_next(instruction, map, current_pos, count):

    """if instruction == 'L':
        for idx, map_i in enumerate(map):
            if map_i[0] == current_pos[1][0]:
                current_pos = map[idx]
                return current_pos
    elif instruction == 'R':
        for idx, map_i in enumerate(map):
            if map_i[0] == current_pos[1][1]:
                current_pos = map[idx]
                return current_pos"""
    if instruction == 'L':
        return map[current_pos][0]
    elif instruction == 'R':
        return map[current_pos][1]

def main():
    with open("2023/inputs/day8.txt") as file:
        lines = file.readlines()
    instructions, map = convert_to_map(lines)
    a_nodes = list()
    for key in map.keys():
        if key[2] == 'A':
            a_nodes.append(key)
    print(a_nodes)
    found = False
    count = 0
    
    while not found:
        for instruction in instructions:
            print(count)
            count += 1
            all_z = True
            for idx, node in enumerate(a_nodes):
                a_nodes[idx] = check_next(instruction, map, node, count)
                if a_nodes[idx][2] != 'Z':
                    all_z = False

            if all_z == True:
                found = True
                break
    print(count)



if __name__ == "__main__":
    main()
