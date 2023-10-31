# item class to create new item
class Item:
    def __init__(self,item = None, next = None):
        self.item = item
        self.next = next 

# stack class to implement stack
class Stack:

# init method to initialize instance object variables
    def __init__(self,start = None):
        self.start = start

# method to check whether stack is empty or not
    def is_empty(self):
        return self.start == None

# method to push items into top of stack 
    def push(self,data):
        N = Item(data,self.start)
        self.start = N

# method to pop item from the top of stack
    def pop(self):
        if not self.is_empty():
            print('deleted item is',self.start.item)
            self.start = self.start.next
        else:
            raise IndexError(" Stack is empty")

# method to check the top of stack
    def top(self):
        if not self.is_empty():
            print('top of stack is',self.start.item)  
        else:
            raise IndexError("stack is empty")

# method to find size of stack
    def size(self):
        if not self.is_empty():
            count = 0
            temp = self.start
            while temp is not None:
                count = count + 1
                temp = temp.next

            return count
        else:
            raise IndexError("stack is empty")

# method to display the stack 
    def display(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next

# instance object of stack() class
obj = Stack()

obj.push(100)
obj.push(99)
obj.push(98)
obj.push(97)
obj.push(96)

print('stack is ==>',end=" ") 
obj.display()

print()
obj.pop()

obj.top()
print('size of stack is',obj.size())
obj.display()