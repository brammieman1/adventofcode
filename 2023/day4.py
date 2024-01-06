    

def day4a():
    with open('2023\input\day4.txt') as f:
        cards = [card.rstrip() for card in f]
    total_points = 0

    for card in cards:
        winning_numbers, my_numbers = card.split(" | ")
        winning_numbers = winning_numbers.split(': ')[-1].strip().replace("  "," ")
        winning_numbers = [eval(i) for i in winning_numbers.split(" ")]

        my_numbers = my_numbers.strip().replace("  ", " ")
        my_numbers = [eval(i) for i in my_numbers.split(" ")]

        i = 0
        for wnr in winning_numbers:
            if wnr in my_numbers:
                i = i + 1
        if i>=1: 
            points = 2**(i-1)
        else:
            points = 0

        total_points = total_points + points


    print(total_points)

if __name__ == "__main__":
    day4a()