#Stack

# eshe che to tam ya zabil

#Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None
    
    def enqueue(self,item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return removed_data
    
    def peek(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.front.data
    
    def size(self):
        return self._size
    
    def display(self):
        current = self.front
        items = []
        while current:
            items.append(current.data)
            current = current.next
        print('Queue: ', items)