def main():
    file = open("2023/inputs/day5.txt", "r")
    lines = file.read().splitlines()
    seeds = lines[0].split(":")[1].split(" ")[1:]
    seeds_ranges = list()
    for i in range(0, len(seeds), 2):
        seeds_ranges.append((seeds[i], seeds[i+1]))
    
    map_list = list()
    empty_line = False
    category = 0
    category_list = list()

    for i in range(1, len(lines)):
        if lines[i] == "":
            map_list.append(category_list)
            category_list = list()
            empty_line = True
            continue
        elif empty_line is True:
            empty_line = False
            continue
        else:
            # print(lines[i].split(" "))
            lines_location = lines[i].split(" ")
            category_list.append(((int(lines_location[0])), int(lines_location[1]), int(lines_location[2])))
                # print(lines_location[0])
    map_list.append(category_list)
    locations_list = list()
    for seed in seeds_ranges:
        for i in range(int(seed[1])):
            current_value = int(seed[0]) + i
            for category in map_list:
                for value in category:
                    if value[1] <= current_value and value[1] + value[2] > current_value:
                        current_value = value[0] + (current_value - value[1])
                        break
            # print(current_value)
            locations_list.append(int(current_value))
    print(min(locations_list))

if __name__ == "__main__":
    main()
