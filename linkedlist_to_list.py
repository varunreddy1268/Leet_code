# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import time
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) ->Optional[ListNode]:
        start=time.time()
        main_list1,main_list2=[],[]
        def conv_list(x):
            temp,p=x,""
            p=str(temp.val)
            while (temp):
                p=p+str(temp.val)
                temp=temp.next
            return p
        main_list1,main_list2=int(conv_list(l1)[1:][::-1]),int(conv_list(l2)[1:][::-1])
        def stringToListNode(stringTotal):
            previousNode = None
            first = None
            for i in stringTotal:
                currentNode = ListNode(i)
                if first is None:
                    first = currentNode
                if previousNode is not None:
                    previousNode.next = currentNode
                previousNode = currentNode
            return first
        
        res=stringToListNode(str(main_list1+main_list2)[::-1])
        return res
"""
342
465

807
708
"""
