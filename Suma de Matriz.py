matriz = [
    [1,1,1],
    [1,1,1],
    [1,1,1],
]
sum = 0

for i in range(0,len(matriz),1):
    for j in range(0,len(matriz),1):
        sum += matriz[i][j]

print(sum)