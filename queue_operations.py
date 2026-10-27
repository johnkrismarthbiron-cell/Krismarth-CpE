class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = node
            self.rear = node
            return

        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue from an empty queue')

        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def values(self):
        items = []
        current = self.front
        while current is not None:
            items.append(current.value)
            current = current.next
        return items
