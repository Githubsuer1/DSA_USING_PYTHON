# stack class extending the list class
class Stack(list):

# method to check whether stack is empty or not
    def is_empty(self):
        return len(self)==0

# push method to insert data on the top of stack 
    def push(self,data):
        self.append(data)

# pop method to delete data from top of stack 
    def pop(self):
        if not self.is_empty():
            super().pop()       # here super keyword is used to avoid from recursion, actually super class always points to the parent class.
        else:
            raise IndexError("Stack is empty")

# method to get the size of stack
    def size(self):
        if not self.is_empty():
            return len(self)

# method to find the top of stack 
    def top(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")

# method to display the stack
    def display(self):
        if not self.is_empty():
            for i in self:
                print(i,end=" ")

#restricting the stack class by overriding the insert method to not use the built in "insert" method.
    def insert(self,index,data):
        raise AttributeError("This method does not exist in this data structure")

s1 = Stack()
s1.push(8)
s1.push(9)
s1.push(10)

# s1.insert(0,12)       this function will generate attribute error as it is restricted to work.

print('top of stack is',s1.top())
s1.pop()
print('top of stack is',s1.top())
s1.display()