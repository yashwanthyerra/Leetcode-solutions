from collections import deque
class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.dq = deque()
    def enQueue(self, value: int) -> bool:
        if len(self.dq)<self.k:
            self.dq.append(value)
            return True
        return False
    def deQueue(self) -> bool:
        if self.dq:
            self.dq.popleft()
            return True
        return False
    def Front(self) -> int:
        if not self.dq :
            return -1
        return self.dq[0]
    def Rear(self) -> int:
        if not self.dq:
            return -1
        return self.dq[-1]
    def isEmpty(self) -> bool:
        return len(self.dq) ==0
    def isFull(self) -> bool:
        return  len(self.dq)==self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()