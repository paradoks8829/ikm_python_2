from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, n) -> str:
        new_node = Node(n)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return "ok"
    
    def pop(self) -> str:
        if self.head is None:
            return "error"
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return str(val)
    
    def front(self) -> str:
        if self.head is None:
            return "error"
        return str(self.head.val)
    
    def get_size(self) -> str:
        return str(self.size)
    
    def clear(self) -> str:
        self.head = None
        self.tail = None
        self.size = 0
        return "ok"
    
    def exit(self) -> str:
        return "bye"