class ArrayStack:
    def __init__(self, size=2):
        self.MAXSIZE = size
        self.index = -1
        self.data = [None] * size

    def push(self, value):
        if self.index < self.MAXSIZE-1:
            self.index += 1
            self.data[self.index] = value
            return value

    def pop(self):
        if self.index > -1:
            value = self.data[self.index]
            self.data[self.index] = None
            self.index -= 1
            return value

    def peek(self):
        if self.index > -1:
            return self.data[self.index]

    def isEmpty(self):
        return self.index == -1



stack = ArrayStack(16)
print(stack.data)

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek()) # 3
print(stack.data)
print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1
print(stack.pop()) # None
