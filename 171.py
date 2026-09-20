input = "AB"

def character(input):


  result = 0
  for i in input:

    mapping = ord(i)-64

    result = result * 26 + mapping

  return result


print(character(input))