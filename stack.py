class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() < 1:
            return None
        return self.stack.pop(0)

    def push(self, value):
        return self.stack.insert(0, value)
                                  
    def peak(self):
        if self.size() < 1:
            return None
        return self.stack[0]

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
