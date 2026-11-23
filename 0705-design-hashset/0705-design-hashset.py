class ListNode:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.head = None
        
    def add(self, key: int) -> None:

        if self.contains(key):
            return
        
        nextNode = ListNode(key)

        if self.head is None:
            self.head = nextNode

        else:

            point = self.head
            while point.next:
                point = point.next

            point.next = nextNode
        
        

    def remove(self, key: int) -> None:

        if self.contains(key):
            
            if self.head.val == key:
                self.head = self.head.next
                    
            else:
                point = self.head
                while point.next:
                    if point.next.val == key:
                        point.next = point.next.next
                        break
                    point = point.next

        

    def contains(self, key: int) -> bool:

        point = self.head

        while point:

            if point.val == key:
                return True
            point = point.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)