class Deque:
    def __init__(self):
        self.my_list = []

    def is_empty(self):
        return len(self.my_list) == 0
     
    def insert_front(self,data):
        self.my_list.insert(0,data)
    
    def insert_rear(self,data):
        self.my_list.append(data)

    def delete_front(self):
        if self.is_empty():
            raise IndexError('Oh oh, Deque is empty!')
        else:
            self.my_list.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Oh oh, Deque is empty!')
        else:
            self.my_list.pop()

    def get_front(self):
        if self.is_empty():
            raise IndexError('Oh oh, Deque is empty!')
        else:
            return self.my_list[0]

    def get_rear(self):
        if self.is_empty():
            raise IndexError('Oh oh, Deque is empty!')
        else:
            return self.my_list[-1]

    def size(self):
        if self.is_empty():
            raise IndexError('Oh oh, Deque is empty!')
        else:
            return len(self.my_list)

    def display(self):
        if self.is_empty():
            raise IndexError('Oh oh, Deque is empty!')
        else:
            print(self.my_list)

obj = Deque()

obj.insert_front(30)
obj.insert_front(20)
obj.insert_front(10)
print('size is ',obj.size())        # output:- size is  3

obj.insert_rear(40)
obj.insert_rear(50)
obj.insert_rear(60)
print('size is ',obj.size())        # output:- size is  6

print('front item',obj.get_front()) # output:- front item 10
print('rear item',obj.get_rear())   # output:- rear item 60

print('after deletion')

obj.delete_front()
obj.delete_rear()
print('size is ',obj.size())        # output:- size is  4

print('front item',obj.get_front()) # output:- now front item 20
print('rear item',obj.get_rear())   # output:- now rear item 50

obj.display()                       # output:- [20, 30, 40, 50]





