num = 19

def happy_no(num):

  seen = set()

  while num != 1:
    if num in seen:
      return False

    seen.add(num)
    add = 0 
    while num > 0:

      

      add += (num % 10)**2

      num  = num //10

    num = add

  return True


print(happy_no(num))

 
