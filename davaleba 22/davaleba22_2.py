class Queue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("Queue is empty")
            return None
        return self.items[0]

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
print(q.pop())  # Must return 1
