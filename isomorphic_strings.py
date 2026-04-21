s = "egg"
t = "add"

d1 = {}
d2 = {}

for i in range(len(s)):
    if s[i] in d1 and d1[s[i]] != t[i]:
        print(False)
        break

    if t[i] in d2 and d2[t[i]] != s[i]:
        print(False)
        break

    d1[s[i]] = t[i]
    d2[t[i]] = s[i]

else:
    print(True)