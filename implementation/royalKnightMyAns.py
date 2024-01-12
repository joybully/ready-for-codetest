position = input()

rowChar = position[1]
columnChar = position[0]

row = ['1','2','3','4','5','6','7','8']
column = ['a','b','c','d','e','f','g','h']

moveRow = [-2, 2, 1, -1, -2, 2, 1, -1]
moveColumn = [1, 1, 2, 2, -1, -1, -2, -2]

for i in range(8):
    if(rowChar==row[i]):
        currentRow = i

for i in range(8):
    if(columnChar==column[i]):
        currentColumn = i

result = 0

for i in range(8):
    if currentRow+moveRow[i]<0 or currentRow+moveRow[i]>7 or currentColumn+moveColumn[i]<0 or currentColumn+moveColumn[i]>7:
        continue
    else:
        result+=1

print(result)