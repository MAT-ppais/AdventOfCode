def main():
    with open("inputs/day6.txt") as file:
        lines = file.readlines()
        time = list(map(int, lines[0].split()[1:]))
        distance = list(map(int, lines[1].split()[1:]))  
    time_total = ""
    distance_total = ""
    for time in time:
        time_total += str(time)
    time_total = int(time_total)
    for distance in distance:
        distance_total += str(distance)
    distance_total = int(distance_total)
    print(time_total)
    print(distance_total)
    local_count = 0
    time_new_record = list()
    how_much_ways = 0
    
    for i in range(time_total):
        remaining_time = time_total
        remaining_time -= i
        local_count = i * remaining_time
        if local_count > distance_total:
            how_much_ways += 1
    print(how_much_ways)
    

if __name__ == "__main__":
    main()
