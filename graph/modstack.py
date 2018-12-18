class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        return self.stack.append(value)  
                                  
    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1] 

    def size(self):
        return len(self.stack)

    def balans(self, s1):
        s2 = Stack()
        for i in range(len(s1)):
            if s1[i] == "(":
                s2.push("(")
            elif s1[i] == ")" and s2.peak() == "(":
                s2.pop()
        if s2.size() == 0:
            print("balans")
        else:
            print("ne balans")

    def s4et(self, vir):
        s = vir.split()
        s1 = Stack()
        s2 = Stack()
        for i in range(len(s)):
            s1.push(s[i])
            if s[i] == "+":
                while s2.size() > 1:
                    s2.push(s2.pop() + s2.pop())
                s1.pop()
            elif s[i] == "*":
                while s2.size() > 1:
                    s2.push(s2.pop() * s2.pop())
                s1.pop()
            elif s[i] == "=":
                print("Sum = ", s2.pop())
            else:
                s2.push(int(s1.pop()))

    def chered(self, s1, n):
        for i in range(n):
            self.push(s1.pop())

        while self.size() > 0:
            print(self.pop())

    def clear_stack(self):
        while len(self.stack) > 0:
            self.pop()