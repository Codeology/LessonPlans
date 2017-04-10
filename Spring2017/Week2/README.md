## Lesson

"Linked lists are like Legos" -- Dickson Tsai

A linked list is like a series of blocks that are connected to each
other in a series, and each block has some information attached to it.
Just as a lego brick has a size, a shape, a color, etc., a node
in a linked list can have a value and other properties.

Questions involving linked list manipulations are tricky because
it may be easy to visualize a solution but harder to actually translate
your thoughts down into code for. Many linked list manipulation questions
can be solved both iteratively and recursively, and it's useful to try
different perspectives when you're practicing!

Here's a quick sample of a singly Linked List class implementation:

```python
class Node:
    def __init__(self, value):
        self.value = value # you can put pretty much anything here
        self.next = None

class SinglyLinkedList:
    def __init__(self, node):
        self.head = node
        self.last = node

    def append(self, node):
        self.last.next = node
        self.last = self.last.next

a = Node(1)
b = Node('a')
c = Node(Node(2)) # node-ception

lst = SinglyLinkedList(a)
lst.append(b)
lst.append(c)

# lst looks like this: head->[1]->[2]->[3]->None
print(lst.head.value) # 1
print(lst.head.next.value) # a
print(lst.head.next.next.value) # <__main__.Node instance at 0x10ffacf80>
```

As simple as they are, there are different kinds of linked lists.
Doubly linked lists make it easy for you to navigate forwards and
backwards in the list. Circular linked lists have tail nodes that link
back to the head node in the list. You can read more about linked
lists [here](https://en.wikipedia.org/wiki/Linked_list#Basic_concepts_and_nomenclature).

## Demo

Anyone know how to reverse a linked list?  
How about deleting a node in a linked list?

## Mock Interview Questions (work in pairs and raise your hand for check off!)

* [(Easy) Remove duplicates](./questions/question-remove-duplicates.md)
* [(Easy) Delete a node](./questions/question-delete-middle-node.md) | [Solution](./solutions/solution-delete-middle-node.md)
* [(Easy) Palindrome](./questions/question-palindrome.md) | [Solution](./solutions/solution-palindrome.md)
* [(Medium) Sum Lists](./questions/question-sum-lists.md) | [Solution](./solutions/solution-sum-lists.md)
* [(Medium) Loop Detection](./questions/question-loop-detection.md) | [Solution](./solutions/solution-loop-detection.md)
* [(Medium) Intersection](./questions/question-intersection.md) | [Solution](./solutions/solution-intersection.md)
