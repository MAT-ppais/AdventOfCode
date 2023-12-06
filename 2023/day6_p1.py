def main():
    with open("inputs/day6.txt") as file:
        lines = file.readlines()
        time = list(map(int, lines[0].split()[1:]))  # Skip the first word 'Time:'
        distance = list(map(int, lines[1].split()[1:]))  # Skip the first word 'Distance:'
    print(time)
    print(distance)
    local_count = 0
    time_new_record = list()
    how_much_ways = 0
    
    for idx, time in enumerate(time):
        for i in range(time):
            remaining_time = time
            remaining_time -= i
            local_count = i * remaining_time
            if local_count > distance[idx]:
                how_much_ways += 1
        time_new_record.append(how_much_ways)
        how_much_ways = 0
    multiply_count = 1
    for record in time_new_record:
        multiply_count = multiply_count * record
    print(multiply_count)

    

if __name__ == "__main__":
    main()
