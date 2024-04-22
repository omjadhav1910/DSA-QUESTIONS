
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    if not head:
        print(" ")
        return

    current = head

    while current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    current = head
    while current:
        print(current.val, end=" ")
        current = current.next

def create_linked_list():
    input()  # Discard the first line since it's the size of the list
    values = input().split()
    if not values:
        return None

    head = ListNode(int(values[0]))
    current = head
    for val in values[1:]:
        current.next = ListNode(int(val))
        current = current.next

    return head

if __name__ == "__main__":
    head = create_linked_list()
    remove_duplicates(head)
