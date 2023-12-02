def main():
    file = open("inputs/day2.txt", "r")
    lines = file.readlines()
    power_sum = 0
    for index, line in enumerate(lines):
        parts = line.split(":")
        game = parts[1].strip()
        game_parts = game.split(";")
        min_red = min_green = min_blue = 0
        for part in game_parts:
            numbers = [(int(num.split()[0]), num.split()[1]) for num in part.split(",")]
            for number in numbers:
                if number[1] == 'green':
                    min_green = max(min_green, number[0])
                elif number[1] == 'blue':
                    min_blue = max(min_blue, number[0])
                elif number[1] == 'red':
                    min_red = max(min_red, number[0])
        power_sum += min_red * min_green * min_blue
    
    print(power_sum)
    
if __name__ == "__main__":
    main()
