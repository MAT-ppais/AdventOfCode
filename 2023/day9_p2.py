def main():
    with open("2023/inputs/day9.txt") as file:
        lines = file.readlines()
    values = list()
    a = list()
    count = 0
    for line in lines:
        values.append(line.strip().split(" "))
    for value_line in values:
        count += next_value(value_line)
    print(count)

def next_value(value_line):
    a = value_line
    last_values = list()
    last_values.append([int(i) for i in a])
    first_values = 0
    while(True):
        b = list()
        for i in range(len(a) - 1):
            b.append(int(a[i + 1]) - int(a[i]))
        a = b
        last_values.append(a)
        if all(i == a[0] for i in a):
            break
    for i in range(len(last_values) - 1, -1, -1): 
        first_values = last_values[i][0] - first_values 
    return first_values

if __name__ == "__main__":
    main()
