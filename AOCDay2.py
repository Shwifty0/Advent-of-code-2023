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