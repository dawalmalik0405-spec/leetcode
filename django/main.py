input = [1,0,0,1,0,1,0,0,1]


positions = []
adjusted  = []
moves = 0

for i in range(len(input)):

  if input[i] == 1:
    positions.append(i)

for i in range(len(positions)):

  adjusted.append(positions[i] - i)
  adjusted.sort()

  mean = adjusted[len(adjusted)//2]

for x in adjusted:

  moves += abs(x- mean)

print(moves)








    


    

    