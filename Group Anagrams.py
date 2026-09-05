s  = ["eat", "tea", "tan", "ate", "nat", "bat"]



def grpOfAnagrams(s):

  e = {}

  for i in s:

    l = "".join(sorted(i))

    if l in e:
      e[l].append(i)

    else:

      e[l] = [i]

  return e.values()



print(grpOfAnagrams(s))








 

  
