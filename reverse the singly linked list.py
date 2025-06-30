class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Step 1: Create linked list from values
values = [1, 7, 9, 10, 100]
if not values:
    head = None
if values:
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
# Step 2: Class to reverse the linked list
class ReverseList:
    def rev(self, head: ListNode):
        prev = None
        curr = head
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev  # new head of the reversed list

# Step 3: Reverse and print
obj = ReverseList()
reversed_head = obj.rev(head)

# Step 4: Print the reversed list
curr = reversed_head
while curr:
    print(curr.val, end=" ")
    curr=curr.next
