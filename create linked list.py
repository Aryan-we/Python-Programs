class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Take input values
values = [1,7,9,10,100]

# Create linked list
if not values:
    head = None
else:
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

# Convert linked list to Python list
linked_list_as_list = []
current = head
while current:
    linked_list_as_list.append(current.val)
    current = current.next

# Display the list
print("Linked list as Python list:", linked_list_as_list)
