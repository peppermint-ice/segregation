import random

def CreateRandomField(x, y, tol, dens, shareOfO):
    gameField = []
    dotxy = []
    for i in range(y):
        for j in range(x):
            randomNumber = random.randint(1,100)
            if randomNumber <= dens:
                if randomNumber <= (shareOfO * dens / 100):
                    dotxy.append('⧠')
                else:
                    dotxy.append('■')
            else:
                dotxy.append(' ')
        gameField.append(dotxy)
        dotxy = []
    return gameField

def CalcHappyness(field):
    happinessField = []
    for i in range(len(field)):
        happinessRow = []
        for j in range(len(field[i])):
            happiness = 0
            if field[i][j] == ' ':
                happiness = ' '
            # not edge
            elif (i - 1 >= 0 and
                    i + 1 <= (len(field) - 1) and
                    j - 1 >= 0 and
                    j + 1 <= (len(field[i]) - 1)):
                if field[i - 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[i - 1][j] == field[i][j]:
                    happiness += 1
                if field[i - 1][j + 1] == field[i][j]:
                    happiness += 1
                if field[i][j - 1] == field[i][j]:
                    happiness += 1
                if field[i][j + 1] == field[i][j]:
                    happiness += 1
                if field[i + 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[i + 1][j] == field[i][j]:
                    happiness += 1
                if field[i + 1][j + 1] == field[i][j]:
                    happiness += 1
            # bot
            elif (i + 1 == (len(field)) and j != 0 and j != len(field[i]) - 1):
                if field[i - 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[i - 1][j] == field[i][j]:
                    happiness += 1
                if field[i - 1][j + 1] == field[i][j]:
                    happiness += 1
                if field[i][j - 1] == field[i][j]:
                    happiness += 1
                if field[i][j + 1] == field[i][j]:
                    happiness += 1
                if field[0][j - 1] == field[i][j]:
                    happiness += 1
                if field[0][j] == field[i][j]:
                    happiness += 1
                if field[0][j + 1] == field[i][j]:
                    happiness += 1
            # top
            elif (i - 1 == -1  and j != 0 and j != len(field[i]) - 1):
                if field[len(field) - 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[len(field) - 1][j] == field[i][j]:
                    happiness += 1
                if field[len(field) - 1][j + 1] == field[i][j]:
                    happiness += 1
                if field[i][j - 1] == field[i][j]:
                    happiness += 1
                if field[i][j + 1] == field[i][j]:
                    happiness += 1
                if field[i + 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[i + 1][j] == field[i][j]:
                    happiness += 1
                if field[i + 1][j + 1] == field[i][j]:
                    happiness += 1
            # left
            elif (j - 1 == -1 and i != 0 and i != len(field) - 1):
                if field[i - 1][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[i - 1][j] == field[i][j]:
                    happiness += 1
                if field[i - 1][j + 1] == field[i][j]:
                    happiness += 1
                if field[i][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[i][j + 1] == field[i][j]:
                    happiness += 1
                if field[i + 1][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[i + 1][j] == field[i][j]:
                    happiness += 1
                if field[i + 1][j + 1] == field[i][j]:
                    happiness += 1
            # right
            elif (j + 1 == (len(field[i])) and i != 0 and i != len(field) - 1):
                if field[i - 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[i - 1][j] == field[i][j]:
                    happiness += 1
                if field[i - 1][0] == field[i][j]:
                    happiness += 1
                if field[i][j - 1] == field[i][j]:
                    happiness += 1
                if field[i][0] == field[i][j]:
                    happiness += 1
                if field[i + 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[i + 1][j] == field[i][j]:
                    happiness += 1
                if field[i + 1][0] == field[i][j]:
                    happiness += 1
            # bot left
            elif (i + 1 == (len(field)) and j - 1 == -1):
                if field[len(field) - 2][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[i - 1][j] == field[i][j]:
                    happiness += 1
                if field[i - 1][j + 1] == field[i][j]:
                    happiness += 1
                if field[len(field) - 1][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[i][j + 1] == field[i][j]:
                    happiness += 1
                if field[0][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[0][j] == field[i][j]:
                    happiness += 1
                if field[0][j + 1] == field[i][j]:
                    happiness += 1
            # bot right
            elif (i + 1 == (len(field)) and j + 1 == (len(field[i]))):
                if field[i - 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[i - 1][j] == field[i][j]:
                    happiness += 1
                if field[len(field) - 2][0] == field[i][j]:
                    happiness += 1
                if field[i][j - 1] == field[i][j]:
                    happiness += 1
                if field[i][0] == field[i][j]:
                    happiness += 1
                if field[0][j - 1] == field[i][j]:
                    happiness += 1
                if field[0][j] == field[i][j]:
                    happiness += 1
                if field[0][0] == field[i][j]:
                    happiness += 1
            # top left
            elif (i - 1 == -1 and j - 1 == -1):
                if field[len(field) - 1][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[len(field) - 1][j] == field[i][j]:
                    happiness += 1
                if field[len(field) - 1][j + 1] == field[i][j]:
                    happiness += 1
                if field[i][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[i][j + 1] == field[i][j]:
                    happiness += 1
                if field[1][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[i + 1][j] == field[i][j]:
                    happiness += 1
                if field[i + 1][j + 1] == field[i][j]:
                    happiness += 1
            # top right
            elif (i - 1 == -1 and j + 1 == (len(field[i]))):
                if field[len(field) - 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[len(field) - 1][j] == field[i][j]:
                    happiness += 1
                if field[len(field) - 1][len(field[i]) - 1] == field[i][j]:
                    happiness += 1
                if field[i][j - 1] == field[i][j]:
                    happiness += 1
                if field[i][0] == field[i][j]:
                    happiness += 1
                if field[i + 1][j - 1] == field[i][j]:
                    happiness += 1
                if field[i + 1][j] == field[i][j]:
                    happiness += 1
                if field[i + 1][0] == field[i][j]:
                    happiness += 1
            happinessRow.append(happiness)
        happinessField.append(happinessRow)


    return happinessField


def Moving(field, happinessField, tol):
    space = []
    spacesList = []
    unhappy = []
    unhappyList = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == ' ':
                space.append(i)
                space.append(j)
                spacesList.append(space)
                space = []
    for i in range(len(happinessField)):
        for j in range(len(happinessField[i])):
            if happinessField[i][j] != ' ':
                if happinessField[i][j] / 8 * 100 <= tol:
                    unhappy.append(i)
                    unhappy.append(j)
                    unhappyList.append(unhappy)
                    unhappy = []
    # print('spacesList')
    # print(spacesList)
    # print('unhappyList')
    # print(unhappyList)

    randomsTriggeringMoving = []
    spacesToMoveTo = []
    while len(randomsTriggeringMoving) <= (len(spacesList) - 1) and len(randomsTriggeringMoving) <= (len(unhappyList) - 1):
        randNum = random.randint(0, len(unhappyList) - 1)
        if randNum not in randomsTriggeringMoving:
            randomsTriggeringMoving.append(randNum)
    # print('randomsTriggeringMoving')
    # print(randomsTriggeringMoving)

    while len(spacesToMoveTo) <= (len(spacesList) - 1) and len(spacesToMoveTo) <= (len(unhappyList) - 1):
        randNum = random.randint(0, len(spacesList) - 1)
        if randNum not in spacesToMoveTo:
            spacesToMoveTo.append(randNum)
    # print("spacesToMoveTo")
    # print(spacesToMoveTo)

    for i in range(len(randomsTriggeringMoving) - 1):
        blanki = spacesList[spacesToMoveTo[i]][0]
        blankj = spacesList[spacesToMoveTo[i]][1]
        movingi = unhappyList[randomsTriggeringMoving[i]][0]
        movingj = unhappyList[randomsTriggeringMoving[i]][1]
        field[blanki][blankj] = field[movingi][movingj]
        field[movingi][movingj] = ' '

    return field


def PrintTheField(field):
    for row in field:
        for elem in row:
            print(elem, end=' ')
        print()


x = int(input('enter x:'))
y = int(input('enter y:'))
tol = float(input('enter tolerance:'))
dens = float(input('enter density:'))
shareOfO = float(input('enter share of group 1:'))

print('field size:', x, ':', y)
print('density:', dens)
print('tolerance:', tol)
print('share of the first group:', shareOfO)
for i in range(5):
    print('')

startingField = CreateRandomField(x, y, tol, dens, shareOfO)
PrintTheField(startingField)
happinessField = CalcHappyness(startingField)
print('')
PrintTheField(CalcHappyness(startingField))
print('')
movedField = Moving(startingField, happinessField, tol)
PrintTheField(movedField)

for i in range(200):
    happinessField = CalcHappyness(movedField)
    movedField = Moving(movedField, happinessField, tol)
    PrintTheField(movedField)
