Input =  [3, 0, 1, 2, 5, 7, 8, 4]


def missing_no(input):

  result = 0
  
  for i in range(len(input)):
    result ^= i
    result ^= input[i]

  result ^= len(input)

  return result


print(missing_no(Input))
    







