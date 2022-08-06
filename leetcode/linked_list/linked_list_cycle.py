# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use two pointers, one moving double the speed of other
        # if pointers == each other, return true
                
        if head == None:
            return False
        elif head.next == None:
            return False
        
        p1 = head
        p2 = head.next
        
        while p2 != None:
            if p1 == p2:
                return True
            
            p2 = p2.next
            p1 = p1.next
            
            if p2 != None:
                p2 = p2.next
                
        return False