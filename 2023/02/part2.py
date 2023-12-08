total = 0
with open("2023/02/input.txt") as f:
    for i, line in enumerate(f.readlines()):
        red = 0
        green = 0
        blue = 0
        _, line = line.split(":")
        line = line.strip()
        plays = line.split(";")
        for play in plays:
            for batch in play.split(","):
                count, color = batch.strip().split(" ")
                count = int(count)
                if color == "red":
                    red = max(red, count)
                if color == "green":
                    green = max(green, count)
                if color == "blue":
                    blue = max(blue, count)
        total += red * green * blue
print(total)
