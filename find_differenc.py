s = "abcd"
t = "abcde"

def find(s,t):

  result = 0
  for i in s:
    result ^= ord(i)

  for j in t:
    result ^= ord(j)


  out = chr(result)

  return out

print(find(s, t))
