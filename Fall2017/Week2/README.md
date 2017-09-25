# Week 2 Topic: Linked Lists
## Lesson Overview

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

## Mock Interview Questions Practice

* [Delete a node](./questions/question-delete-middle-node.md)
* [Remove duplicates](./questions/question-remove-duplicates.md)

## Workshop Overview

* We reviewed the two practice problems above, and also went over singly linked list reversal (both iteratively and recursively) and finding the loop in a linked list.
* [Here](https://docs.google.com/presentation/d/1MnqXe4V4DQ_5KlWF98VAgynlQIl9rfOtFOdAyDjdDZM/edit?usp=sharing) are the slides


## Additional Practice

### Linked List Manipulation

Here are some links for additional linked list manipulation questions for practice. 

* [Deleting a node at a given position](http://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/)
* [Delete last occurence of key](http://www.geeksforgeeks.org/delete-last-occurrence-of-an-item-from-linked-list/)
* [Merge two sorted linked lists](https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists)
* [Add two numbers represented by linked lists](https://leetcode.com/problems/add-two-numbers/)

Also, it's important to familiarize yourself with **doubly linked lists** as well. A doubly linked list contains an extra pointer for each node pointing to the previous node. 
* Advantages:
	* Allows both forward and backward list traversal
	* Delete operation in DLL is more efficient if pointer to the node to be deleted is given. In a singly linked list, we need the pointer to the previous node in order to delete a node, which can involve another list traversal to get this previous node (example of this is linked above). In a doubly linked list, we can get the previous node using previous pointer. 
* Disadvantages:
	* Requires extra space for the previous pointer. [Here](http://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-1/) is a memory efficient doubly linked list for those interested. 
	* Requires an extra pointer to keep track of in certain operations. For example, in insertion, we need to modify previous pointers together with next pointers.

Try reversing a doubly linked list for practice:

* [Reverse doubly linked list](http://www.geeksforgeeks.org/reverse-a-doubly-linked-list/)

### Runner Technique
The idea behind the runner technique is that we use two pointers that either move at different speeds or are at a set distance apart when iterating through a list. This is useful in many linked list problems when we need to know an element's position or the length of the list. The runner technique may not be the only way to solve a problem, but can often provide a good solution. You can sometimes tell if your linked list question involves the runner technique when the question involves:

1. Figuring out where two things meet
2. Figuring out the midpoint
3. Figuring out the length

Here are additional problems to try that have possible solutions involving the runner technique: 
* [Find merge point](https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists)
* [Palindrome linked list](https://leetcode.com/problems/palindrome-linked-list/description/)
* [kth element of a linked list](http://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/)






