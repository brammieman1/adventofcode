# Python Advent Of Code Day2

#12 red, 13 green, 14 blue

def day2a():
    with open('2023\input\day2.txt') as f:
        games = [game.rstrip() for game in f]

    game_sum = 0

    for game in games:
        game, temp = game.replace("Game ", "").split(": ")
        sets = temp.split('; ')

        valid_game = True
        for set in sets:
            cubes = set.split(', ')

            for cube in cubes:
                amount, color = cube.split(" ")
                amount = int(amount)

                if color == "red" and amount > 12:
                    valid_game = False
                if color == "green" and amount > 13:
                    valid_game = False
                if color == "blue" and amount > 14:
                    valid_game = False

        if valid_game:
            game_sum = game_sum + int(game)

    print(game_sum)

def day2b():
    with open('2023\input\day2.txt') as f:
        games = [game.rstrip() for game in f]

    game_sum = 0

    for game in games:
        game, temp = game.replace("Game ", "").split(": ")
        sets = temp.split('; ')

        red, green, blue = 0, 0, 0

        valid_game = True
        for set in sets:
            cubes = set.split(', ')
            tmp = []

            for cube in cubes:
                amount, color = cube.split(" ")
                amount = int(amount)

                if color == "red" and amount > red:
                    red = amount
                if color == "green" and amount > green:
                    green = amount
                if color == "blue" and amount > blue:
                    blue = amount

        if valid_game:
            game_sum = game_sum + (red*green*blue)

    print(game_sum)    
    
if __name__ == "__main__":
    day2a()
    day2b()


