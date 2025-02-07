class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.cap = k
        self.sz = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.sz == self.cap:
            return False
        self.sz += 1
        if self.sz == 1:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            temp = self.head
            self.head = Node(value, None, temp)
            temp.prev = self.head
        return True 

    def insertLast(self, value: int) -> bool:
        if self.sz == self.cap:
                return False
        self.sz += 1
        if self.sz == 1:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Node(value, temp, None)
            temp.next = self.tail
        return True

    def deleteFront(self) -> bool:
        if self.sz == 0:
            return False
        self.sz -= 1
        if self.sz > 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
        return True

    def deleteLast(self) -> bool:
        if self.sz == 0:
            return False
        self.sz -= 1
        if self.sz > 0:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
        return True

    def getFront(self) -> int:
        if self.sz == 0:
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.sz == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.sz == 0

    def isFull(self) -> bool:
        return self.sz == self.cap


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()