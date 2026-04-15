digits = [4, 3, 2, 1,1]

result = int(''.join(map(str, digits)))


result +=1 

s  = list(map(int, str(result)))

print(s)

# digits = [4, 3, 2, 11]

# for i in range(len(digits)-1, -1, -1):
#     if digits[i] < 9:
#         digits[i] += 1
#         break
#     digits[i] = 0
# else:
#     digits.insert(0, 1)

# print(digits)