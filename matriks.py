# pertambahan

sum1 = [[2, 4], [5, -6]]
sum2 = [[9, -3], [3, 6]]

print("Penambahan dua matriks")
for x in range(0, len(sum1)):
    print("[", end='')
    for y in range(0, len(sum2)):
        print("{:2d}".format(sum1[x][y] + sum2[x][y]),end='')
        if y < 1:
            print(" ", end='')
    print("]")


print('')
# perkalian
print("Perkalian dua matriks")
mul1 = [[3, 6, 7], [5, -3, 0]]
mul2 = [[1, 1], [2, 1], [3, -3]]
mul3 = 0

for x in range(0, len(mul1)):
    print("[", end='')
    for y in range(0, len(mul1)):
        for z in range(0, len(mul2)):
            mul3 += (mul1[x][z]*mul2[z][y])
        print("{:2d}".format(mul3), end='')
        mul3 = 0
        if y < 1:
            print(" ", end='')
    print("]")

print('')
# transpose
print("Transpos matriks")

trans1 = [[1,2,3], [1,1,3]]
for x in range(0, len(trans1)):
    print("[", end='')
    for y in range(0, len(trans1[0])):
        print(trans1[x][y], end='')
        if y < len(trans1):
            print(" ", end='')
    print("]") 
