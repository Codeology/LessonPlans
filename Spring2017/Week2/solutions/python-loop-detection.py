# quick implementations for testing purposes
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, array):
        self.head = Node(array[0])
        self.last = self.head
        for value in array[1:]:
            self.last.next = Node(value)
            self.last = self.last.next

# return the node at the beginning of a loop
# if there's no loop, return nothing
def detectLoop(linked_list):
    tortoise, hare = linked_list.head, linked_list.head
    while hare != None:
        # move the tortoise once
        tortoise = tortoise.next

        # move the hare twice
        hare = hare.next
        if hare == None:
            return False
        hare = hare.next

        if tortoise == hare: # this checks the references, NOT the node values
            return True
    return False

def tests():
    a = LinkedList([1,2,3])
    a.last.next = a.head # loops at 1
    print(detectLoop(a) == True)

    b = LinkedList([1,2,3,4])
    b.last.next = b.head # loops at 1
    print(detectLoop(b) == True)

    c = LinkedList([1,2,3,4])
    c.last.next = c.head.next # loops at 2
    print(detectLoop(c) == True)

    d = LinkedList([1,2,3,4]) # no loop, so return False
    print(detectLoop(d) == False)

tests()
