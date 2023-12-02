def main():
    file = open("inputs/day2.txt", "r")
    lines = file.readlines()
    count = 0
    for index, line in enumerate(lines):
        parts = line.split(":")
        game = parts[1].strip()
        game_parts = game.split(";")
        gamePossible = True
        for part in game_parts:
            numbers = [(int(num.split()[0]), num.split()[1]) for num in part.split(",")]
            for number in numbers:
                if number[1] == 'green' and number[0] > 13:
                    gamePossible = False
                elif number[1] == 'blue' and number[0] > 14:
                    gamePossible = False
                elif number[1] == 'red' and number[0] > 12:
                    gamePossible = False
        if gamePossible: 
            count += (index + 1)
    
    print(count)
    
if __name__ == "__main__":
    main()
