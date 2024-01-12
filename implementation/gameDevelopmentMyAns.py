def turnLeft(direction):
    direction=-1
    if(direction<0):
        direction = 3
    return direction

mapSizeY, mapSizeX = map(int, input().split())
positionX, positionY, direction = map(int ,input().split())
positionX =- 1
positionY =- 1
data = []
visit = []
directionList = [(-1,0), (0, 1), (1, 0), (0, -1)]
turnNum = 0
move = 0

for i in range(mapSizeX):
    visitColumn = []
    for j in range(mapSizeY):
        visitColumn.append(False)
    visit.append(visitColumn)
visit[positionX][positionY] = True

for i in range(mapSizeX):
    rowData = list(map(int, input().split()))
    data.append(rowData)

while True:
    direction = turnLeft(direction)
    dx = positionX + directionList[direction][0]
    dy = positionY + directionList[direction][1]
    turnNum+=1
    if(visit[dx][dy]==True or data[dx][dy]==1 or dx<0 or dx>=mapSizeX or dy<0 or dy>=mapSizeY):
        if(turnNum>=4):
            dx = positionX - directionList[direction][0]
            dy = positionY - directionList[direction][1]
            if(visit[dx][dy]==True or data[dx][dy]==1 or dx<0 or dx>=mapSizeX or dy<0 or dy>=mapSizeY):
                print(move)
                break
            else:
                turnNum = 0
                move+=1
                positionX = dx
                positionY = dy
        else:
            continue
    else:
        turnNum = 0
        move+=1
        positionX = dx
        positionY = dy