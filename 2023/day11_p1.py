import math

def main():
    with open("2023/inputs/day11.txt") as file:
        lines = file.readlines()
    lines = [line[:-1] for line in lines]
    lines = expand(lines)
    stars = find_stars(lines)
    print(stars)
    
    count = 0
    for i in range(len(stars)):
        for j in range(i, len(stars), 1):
            if i != j:
                print(f"{i},{j} = {(stars[j][0] - stars[i][0]) + (stars[j][1] - stars[i][1])}")
                count += abs(stars[j][0] - stars[i][0]) + abs(stars[j][1] - stars[i][1])
    print(count)


def expand(lines):
    idx_h = list()
    idx_v = list()
    idx_h_count = 0
    for idx, line in enumerate(lines):
        if all(i == line[0] for i in line):
            idx_h.append(idx+idx_h_count)
            idx_h_count += 1
    
    for i in range(len(lines[0])):
        idx_is_v = True
        
        for j in range(len(lines)):
            if lines[j][i] != '.':
                print(f"{i}:{j}")
                idx_is_v = False
                break
        if idx_is_v == True:
            idx_v.append(i)

    for idx in idx_h:
        lines.insert(idx, "..........")
    
    idx_v_count = 0
    for idx in idx_v:
        print(idx)
        for i in range(len(lines)):
            lines[i] = lines[i][:idx+idx_v_count] + '.' + lines[i][idx+idx_v_count:]
            print(lines[i])
        idx_v_count += 1
    
    return lines

def find_stars(lines):
    for line in lines:
        print(line)
    stars = list()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                stars.append((i,j))
    return stars
if __name__ == "__main__":
    main()
