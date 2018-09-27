class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        return self.stack.append(value)  
                                  
    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1] 

    def size(self):
        return len(self.stack)

    def balans(self):
        x = 0
        while self.size() > 0:
            if self.stack[self.size()-1] == ")":
                x += 1
                print("+++",self.pop())
            elif self.stack[self.size()-1] == "(":
                x -= 1
                print("---",self.pop())
        if x == 0:
            print("balans")
        else:
            print("ne balans")
            
stack = Stack()
stack.push("(")
stack.push("(")
stack.push(")")
stack.push(")")
stack.push(")")
stack.push("(")
stack.push("(")
stack.push(")")

print(len(stack.stack))
print("___________")
stack.balans()

