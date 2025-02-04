# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        last_head = head
        prev = None
        curr = head
        flag = True
        final_head = None

        while curr != None:
            curr_head = curr

            # Check if there are more than k elements remaining
            temp = curr
            
            for i in range(k):
                if curr == None:
                    curr = prev
                    prev = None
                    while curr != None:
                        temp = curr.next 
                        curr.next = prev
                        prev = curr
                        curr = temp
                        
                    break
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp
                

            
            if not flag:
                last_head.next = prev
                last_head = curr_head

            if flag:
                flag = False
                final_head = prev
            
            prev = None
        return final_head