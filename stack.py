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

    def balans(self,s1):
        s2 = Stack()
        for j in range (len(s1)):
            s2.push(0)    
        for i in range (len(s1)):
            if s1[i] == "(":
                s2.push("(")
            elif s1[i] == ")":
                s2.pop()
        if s2.size() == len(s1):
            print("balans")
        else:
            print("ne balans")

    def s4et(self,vir):
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
                print("Sum = ",s2.pop())
            else:
                s2.push(int(s1.pop()))
        
            
stack = Stack()
s = "(())))(((((((())))))"
s1 = "8 2 + 5 * ="
stack.s4et(s1)
stack.balans(s)
