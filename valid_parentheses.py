# s ="(]"

# v = []
# pairs = {')': '(', ']': '[', '}': '{'}

# for i in s:
#     if i in "([{":
#       v.append(i)

#       print(v)
#     elif i in ")]}":
#       if not v:
#         print("Invalid")
#         break
#       elif v[-1] == pairs[i] :
#          v.pop()
#       else:
#         print("invalid")
#         break
# else:
#   if not v:
#       print("Valid")
#   else:
#       print("Invalid")


s = "({[]})"


mapping = {
    ")": "(",
    "]": "[",
    "}": "{"
}
def valid_parenthesis(s):
  stack = []


  for i in s:
    if i in "([{":
      stack.append(i)

    else:
      if not stack:
        return False

      if stack[-1] != mapping[i]:
        return False
 
      else:
        stack.pop()

  return not stack


print(valid_parenthesis(s))
      





