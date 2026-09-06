temperatures = [73,74,75,71,69,72,76,73]


def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        # your logic here
        
        while stack and temperatures[i] > temperatures[stack[-1]]:

            s = stack[-1]

            stack.pop()

            answer[s] = i - s

        stack.append(i)

    return answer



print(dailyTemperatures(temperatures))

            

            
