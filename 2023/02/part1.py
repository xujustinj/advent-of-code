total = 0
with open("2023/02/input.txt") as f:
    for i, line in enumerate(f.readlines()):
        ok = True
        _, line = line.split(":")
        line = line.strip()
        plays = line.split(";")
        for play in plays:
            for batch in play.split(","):
                count, color = batch.strip().split(" ")
                count = int(count)
                if (
                    (color == "red" and count > 12)
                    or (color == "green" and count > 13)
                    or (color == "blue" and count > 14)
                ):
                    ok = False
        if ok:
            total += i + 1
print(total)
