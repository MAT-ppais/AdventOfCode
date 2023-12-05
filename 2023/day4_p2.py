def main():
    file = open("inputs/day4.txt", "r")
    lines = file.readlines()
    count = 0
    copies = [1] * 212
    global_count = 0
    global_copies = 0
    for index, line in enumerate(lines):
        card_count = 0
        number_wins = 0
        parts = line.split(":")
        game = parts[1].strip()
        game_parts = game.split("|")
        winner_part = game_parts[0].split(" ")
        numbers = game_parts[1].split(" ")
        list_winners = list()
        numbers_list = list()
        for winner in winner_part:
            if winner != "":
                list_winners.append(winner)
        for number in numbers:
            if number != "":
                numbers_list.append(number)
        # print(numbers_list)    
        for number in numbers_list:
            for winner in list_winners:
                if number == winner:
                    number_wins += 1
                    copies[index + number_wins] += copies[index]
                    if card_count == 0:
                        card_count += 1
                    else:
                        card_count = card_count * 2
        print(copies)
        global_count += card_count
    print(sum(copies))
    
if __name__ == "__main__":
    main()
