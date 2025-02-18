# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or (not head):
            return head

        n = 0
        cur = head
        while cur:
            n+=1
            cur = cur.next
        # print("n:", n)

        k = k%n

        if k==0:
            return head


        steps = n-k
        cur = head
        pre = None
        while steps>0:
            pre = cur
            cur = cur.next
            steps-=1

        pre.next = None

        pre_head = head
        head = cur

        tail = cur
        while k>1:
            tail = tail.next
            k-=1

        if tail:
            tail.next = pre_head

        return head


