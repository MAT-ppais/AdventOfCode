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
    last_values.append(int(a[len(a) - 1]))
    while(True):
        b = list()
        for i in range(len(a) - 1):
            b.append(int(a[i + 1]) - int(a[i]))
        a = b
        last_values.append(b[len(b)-1])
        if all(i == a[0] for i in a):
            break
    return sum(last_values)

if __name__ == "__main__":
    main()
