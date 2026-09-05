s = "anagram"
t = "nagara"

class Solution(object):
    def isAnagram( s, t):

        frequency_s = {}
        frequency_t = {}


        if len(s) != len(t):
            return False

        for character in s:

          frequency_s[character] = frequency_s.get(character, 0) + 1

        for char in  t :
            
          frequency_t[char] = frequency_t.get(char, 0) + 1


        if frequency_t != frequency_s:
              return False

        return True


f = Solution()

print(Solution.isAnagram(s,t))

        

        

            


            
        # increase frequency of character
                
                
            
                   