class Stack:
    def __init__(self,size = 15):
        self.Stack= []
        self.size = size
    def push (self, item):
        if self.size <= len(self.Stack):
            print("The Stack is in Overflow Condition")
        else:
            self.Stack.append(item)
            print("The number",item, "is pushed on the Stack")
    def pop (self):
        if len(self.Stack) <= 0:
            return print ("Stack Underflow!!!")
        else:
            print("Elements popped from stack:")
            print(self.Stack.pop())

    def DisplayStack(self):
        if Stack == []:
            print (" Stack Underflow!!!")
        else:
            return print("Contents of te Stack is: ",self.Stack)




