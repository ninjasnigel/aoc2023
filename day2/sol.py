with open("day2/data.aoc", "r") as file: 
    data = file.readlines()

sack = {"red": 12, "green": 13, "blue": 14}

def check_possible(sack, line):
    games = []
    game, id = line.split(":")[1], line.split(":")[0].split(" ")[1]
    played = game.split(";")

    for game in played:
        gamepieces = {}
        pieces = game.split(",")
        for piece in pieces:
            scan = piece.split(" ")
            if scan[2] not in gamepieces:
                gamepieces[scan[2]] = 0
            gamepieces[scan[2]] += int(scan[1])
        games.append(gamepieces)

    for gamepieces in games:
        for gamepiece in gamepieces:
            print(gamepieces[gamepiece], sack[gamepiece])
            if gamepieces[gamepiece] > sack[gamepiece]:
                return False, id
    return True, id

def min_am(line):
    game, id = line.split(":")[1], line.split(":")[0].split(" ")[1]
    played = game.split(";")
    gamepieces = {}
    
    for game in played:
        pieces = game.split(",")
        for piece in pieces:
            scan = piece.split(" ")
            if scan[2] not in gamepieces:
                gamepieces[scan[2]] = 0
            if gamepieces[scan[2]] < int(scan[1]):
                gamepieces[scan[2]] = int(scan[1])
    return gamepieces

#sol1
possible = 0
for line in data:
    valid, id = check_possible(sack, line.strip("\n"))
    if valid:
        print("valid", line, id)
        possible += int(id)

#sol2
sum = 0
for line in data:
    least_dic = min_am(line.strip("\n"))
    print(least_dic)
    mul = 1
    for key in least_dic:
        mul *= least_dic[key]
    sum += mul

print(sum)