pattern = "abba"
s   = "dog cat cat fish"

def word_pattern(pattern, s):
  map1 = {}
  map2 = {}


  words = s.split()
  if len(pattern) != len(words):
    return False

  for i in range(len(words)):

    if  pattern[i] in map1 and map1[pattern[i]] != words[i]:
      return False

    if  words[i] in map2 and map2[words[i]] != pattern[i]:
      return False


    map1[pattern[i]] = words[i]
    map2[words[i]] = pattern[i]
    
  return True




print(word_pattern(pattern, s))