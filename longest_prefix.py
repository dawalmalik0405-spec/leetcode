words = ["flower","flow","flight"]

prefix = words[0]

result = ""




    
#---------faster----------------

for i in range(len(prefix)):
  
  if(all(i<len(w) and w[i] == prefix[i] for w in words)):

    result += prefix[i]

  else:
    break


  print(result)

  

#___________slower__________________
# for i in range(0, len(prefix)):
#   match = True
#   ##j is word index 
#   for j in range(0, len(words)):
    
#     if i >= len(words[j]):
#       match = False
#       break
     
    
#     elif prefix[i] != words[j][i]:
#       match = False
#       break
#     else:
#       continue
#   if match == False:
#     break
#   else:
#    result += prefix[i]
   

# print(result)


       


