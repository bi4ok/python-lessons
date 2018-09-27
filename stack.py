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

    def s4et(self,vir):
        s = vir.split()
        s1 = Stack()
        s2 = Stack()
        for i in range(len(s)):
            s1.push(s[i])
            print("add")
            if s[i] == "+":
                print("+")
                while s2.size() > 1:
                    print(s2.stack[0])
                    print(s2.stack[1])
                    s2.stack[0] = s2.pop() + s2.stack[0]
                    print(s2.stack[0])
                s1.pop()
            elif s[i] == "*":
                print("*")
                while s2.size() > 1:
                    print("**")
                    print(s2.stack[0])
                    print(s2.stack[1])
                    s2.stack[0] = s2.pop() * s2.stack[0] 
                    print(s2.stack[0])
                s1.pop()
            elif s[i] == "=":
                print("Sum = ",s2.stack[0])
            else:
                s2.push(int(s1.pop()))
        
            
stack = Stack()
stack.push(2)
stack.push(2)
x = "8 2 + 5 * 9 + ="
print("___________")
stack.s4et(x)


