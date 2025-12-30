class Stack:
    def __init__(self):
        self.stack = []
        self.pointer = 0xFF

    def push(self, value):
        self.stack.append(value)
        self.pointer -= 1

    def pop(self):
        if self.stack:
            self.pointer += 1
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")
        
    def reset(self):
        self.stack = []
        self.pointer = 0xFF

    def get_pointer(self):
        return self.pointer
    
    def display(self):
        return self.stack