class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def pop(self):

        if self.output:
             return self.output.pop()


        while self.input:
            self.output.append(self.input.pop())

        return self.output.pop()

    def push(self, x):

        self.input.append(x)


    def peek(self):
        if self.output:
            return self.output[-1]

        while self.input:
            self.output.append(self.input.pop())

        return self.output[-1]


    def empty(self):

        return not self.input and  not self.output

      

        