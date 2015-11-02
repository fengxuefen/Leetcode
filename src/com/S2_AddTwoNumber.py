'''
Created on 2015Äê10ÔÂ30ÈÕ

@author: Fen
'''
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        oriNode=ListNode(0)
        curNode = oriNode
        sumed = 0;
        while(True) :
            if(l1 != None) :
                sumed = sumed + l1.val
                l1 = l1.next
            if(l2 != None) :
                sumed = sumed + l2.val
                l2 = l2.next
            curNode.val = sumed % 10
            sumed = sumed / 10
            if(l1 != None or l2 != None or sumed != 0) :
                curNode.next = ListNode(0)
                curNode = curNode.next
            else :
                break
        return oriNode;
    
        