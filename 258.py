num = 38




def add_digit(num):

  while num >= 10:
    add = 0 
    while num > 0:

      

      add += num % 10

      num  = num //10

    num = add

  return num


print(add_digit(num))

 
