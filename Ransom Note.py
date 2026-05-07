magazine   = "aab"
ransomNote = "aa"

def canConstruct(ransomNote, magazine):
  seen = {}
  for char in magazine:
      if char in seen:
          seen[char] += 1
      else:
          seen[char] = 1

  for cha in ransomNote:
      if cha in seen and seen[cha] > 0:
          seen[cha] -= 1
      else:
          return False
  else:
      return True

print(canConstruct("aa", "aab"))  # True
print(canConstruct("aa", "ab"))   # False    
        