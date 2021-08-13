# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    num1 = []
    num2 = []
    op_num = 0
    op_num1 = 0
    op_num2 = 0
    
    if (not l1.next) and (not l2.next):
        op_num = l1.val + l2.val
        
    num1_next = l1
    
    while (num1_next != None):
        num1.append(num1_next.val)
        num1_next = num1_next.next
        
    num2_next = l2
    
    while (num2_next != None):
        num2.append(num2_next.val)
        num2_next = num2_next.next
        
        
    for idx, digit in enumerate(num1):
        op_num1 += (10 ** idx) * digit
        
    for idx, digit in enumerate(num2):
        op_num2 += (10 ** idx) * digit
        
    op_num = op_num1 + op_num2
    
    op_split = list(map(int,str(op_num)))[::-1]
    
    op_list = ListNode(val=op_split[0], next=None)
    output = op_list
    
    
    for integer in op_split[1:]:
        op_list.next = ListNode(val = integer, next=None)
        op_list = op_list.next
    
    return output

list1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
list2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
list = addTwoNumbers(list1, list2)

print("234 + 564 =", list.next.next.val, list.next.val, list.val)
