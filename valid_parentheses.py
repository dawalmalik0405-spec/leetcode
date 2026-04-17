s ="(]"

v = []
pairs = {')': '(', ']': '[', '}': '{'}

for i in s:
    if i in "([{":
      v.append(i)

      print(v)
    elif i in ")]}":
      if not v:
        print("Invalid")
        break
      elif v[-1] == pairs[i] :
         v.pop()
      else:
        print("invalid")
        break
else:
  if not v:
      print("Valid")
  else:
      print("Invalid")