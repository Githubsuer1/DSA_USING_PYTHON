class Queue(list):

    def is_empty(self):
        return len(self)==0

    def enqueue(self,data):
        self.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.pop(0)
        else:
            raise IndexError("Oh oh, queue is empty!")

    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Oh oh, queue is empty!")

    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Oh oh, queue is empty!")

    def size(self):
        if not self.is_empty():
            return len(self)  
        else:
            raise IndexError("Oh oh, queue is empty!")

    def display(self):
        if not self.is_empty():
            print(self)
        else:
            raise IndexError("Oh oh, queue is empty!")
    
obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.dequeue()
print('front is',obj.get_front())
print('rear is',obj.get_rear())
obj.display()


    