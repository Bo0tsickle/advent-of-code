# Here, we open and read the input file into a string.
inputFile = open("input.txt", "r")
input = inputFile.read()
inputFile.close()

# Here, we create the matrix that will be used to track Santa's movements.
map = [ [ 1, 0 ]
        [ 0, 0 ] ]
santaX, santaY = 0, 0

# This is the loop where the input is read.
for direction in input:
    # This section changes Santa's coordinates depending on his movement.
    if direction == '^':
        santaY += 1
    elif direction == 'v':
        santaY -= 1
    elif direction == '>':
        santaX += 1
    elif direction == '<':
        santaX += 1
    
    # This section checks if Santa is outside the bounds of the matrix. If so, it makes the matrix bigger.
    for i in map:
        if len(i) < santaX:
            i.append(0)
    
    if len(map) < santaY:
        map.append([0] * santaX)
    
    # This sention adds Santa's presents.
    map[santaY][santaX] += 1

# This section creates the count for the amount of presents.
count = 0
for i in map:
    for j in i:
        if j > 0:
            count += 1
print("Your result is: " + count)