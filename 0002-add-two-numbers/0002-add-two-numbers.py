# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummynode for the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        # loop till both lists have no carry over
        while l1 or l2 or carry:
            # get the values of the current nodes, else 0 if list is finished
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # formula for the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10   
            # new node for the result, then move pointer 
            current.next = ListNode(new_digit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next