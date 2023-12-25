# Python Advent Of Code Day1

def day1a():
    with open('2023\input\day1.txt') as f:
        lines = [line.rstrip() for line in f]

    cv_total = 0
    for line in lines:
        cv  = [int(c) for c in line if c.isdigit()]
        if len(cv) > 1:
            cv_total += int(f'{cv[0]}{cv[-1]}')
        if len(cv) == 1:
            cv_total += int(f'{cv[0]}{cv[0]}')
    print(cv_total)

def day1b():
    with open('2023\input\day1.txt') as f:
        lines = [line.rstrip() for line in f]

    lines = [sub.replace('one', 'one1one')
           .replace("two", "two2two")
           .replace("three", "three3three")
           .replace("four", "four4four")
           .replace("five", "five5five")
           .replace("six", "six6six")
           .replace("seven", "seven7seven")
           .replace("eight", "eight8eight")
           .replace("nine", "nine9nine") for sub in lines]


    cv_total = 0
    for line in lines:
        cv  = [int(c) for c in line if c.isdigit()]
        if len(cv) > 1:
            cv_total += int(f'{cv[0]}{cv[-1]}')
        if len(cv) == 1:
            cv_total += int(f'{cv[0]}{cv[0]}')
    print(cv_total)

if __name__ == "__main__":
    day1a()
    day1b()