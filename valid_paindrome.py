c = "racecar"
def valid_palindrom2():
  left = 0
  right = len(c) - 1

  while left <= right:
      if c[left] != c[right]:
          return False

      left += 1
      right -= 1

  return True