s = "A man, a plan, a canal: Panama"


clean = "".join(ch.lower() for ch in s if ch.isalnum())

if clean[::-1] == clean:
    print(True)

else:
    print(False) 
