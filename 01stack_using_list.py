# class Stack used to implement stack using list
class Stack:

# init method to initialize instance object variables
    def __init__(self):
        self.items = []

# method to check whether stack is empty or not
    def is_empty(self):
        return len(self.items) == 0

# push method to insert data on the top of stack 
    def push(self,data):
        self.items.insert(0,data)

# pop method to delete data from top of stack 
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Stack is empty")

# method to get the size of stack
    def size(self):
        return len(self.items)

# method to find the top of stack 
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("stack is empty")

# method to display the stack 
    def display(self):
        if not self.is_empty():
            for i in self.items:
                print(i, end=" ")
        else:
            raise IndexError("Stack is empty")

# instance object of stack class
obj_stack = Stack()

# calling the methods
# obj_stack.push(10)
# obj_stack.push(9)
# obj_stack.push(8)
# obj_stack.push(7)
# obj_stack.push(6)

# obj_stack.display()

# print('removed item is',obj_stack.pop())
# print('removed item is',obj_stack.pop())
# print('removed item is',obj_stack.pop())
# print('removed item is',obj_stack.pop())
# print('removed item is',obj_stack.pop())

# print('item on top is',obj_stack.peek())

print('size of stack is',obj_stack.size())

obj_stack.display()