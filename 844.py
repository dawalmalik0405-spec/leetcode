s = "ab#c"
t = "ad#c"

def check_true(s,t):
    stack = []

    result = ""
    for i in s:
      if i == "#":
      
        if stack:
          stack.pop()

      else:
        stack.append(i)

    result = stack[:]

    stack = []

    for j in t:
      if j == "#":

        if stack:
          stack.pop()

      else:
        stack.append(j)


    return result == stack



print(check_true(s,t))








