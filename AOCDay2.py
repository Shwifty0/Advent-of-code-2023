sample_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


st  = sample_input.split("\n")

limit = {"red":12, "green":13, "blue":14}
total = 0
balls = []
with open("aoc2.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        games = line[line.find(":")+2:].strip().split("; ")
        impossible = False
        for game in games:
            for num in game.split(", "):
                digit, colour = num.split(" ")
                digit = int(digit)
                if digit > limit[colour]:
                    impossible = True
                    break
            if impossible:
                break
        if not impossible:
            total += (i+1)

print(total)