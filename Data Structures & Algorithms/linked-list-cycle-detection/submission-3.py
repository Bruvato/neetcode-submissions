# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        def helper(head, seen) -> bool:
            if not head:
                return False
            
            if head in seen:
                return True
            
            seen.add(head)
            return helper(head.next, seen)
    
        return helper(head, set())
