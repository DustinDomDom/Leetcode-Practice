'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''



class node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = node(2)
node2 = node(4)
node3 = node(3)

node4 = node(5)
node5 = node(6)
node6 = node(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

pointer1 = node1
pointer2 = node4

l1 = []
l2 = []
l3 = []

while pointer1 and pointer2:
    l1.insert(0, pointer1.data)
    l2.insert(0, pointer2.data)
    pointer1 = pointer1.next
    pointer2 = pointer2.next

ret = str(int("".join(map(str, l1))) + int("".join(map(str, l2))))

print(list(ret[::-1]))




