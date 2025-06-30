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
def deleteNode(head,val):
    a=ListNode()
    a.next=head
    b=False
    temp=a
    if(head is None):
        return -1
    while(temp.next!=None):
        if(temp.next.val==val):
            temp.next=temp.next.next
            b=True
        else:
            temp=temp.next
        
    return a.next,b
        
val=int(input("enter the deleted node : "))
a,b=deleteNode(head,val)
if(b==False):
    print("Element is not found")
else:
    while a!=None:
        print(a.val)
        a=a.next


