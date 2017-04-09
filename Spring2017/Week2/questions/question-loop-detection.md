[<- Back to Week 2](..)

## Goal ##
Given a linked list, implement an algorithm that
detects whether this linked list contains a cycle.

## Problem Definitions ##
We are looking for a linked list in which a node's next
pointer points to an earlier node, so as to make a loop in
the linked list.

From [Wikipedia](https://en.wikipedia.org/wiki/Linked_list#Circular_Linked_list):  
![circular linked list][circular]

## Example ##
Input:    A -> B -> C -> D -> E  
Output:   False

Input:    A -> B -> C -> D -> E -> C [the same C as earlier]  
Output:   True

## Solution ##
[Loop Detection](../solutions/solution-loop-detection.md)

## Follow up ##
Now that you can detect whether there is a cycle, can you return
the node where the cycle begins?

## Example ##
Input:    A -> B -> C -> D -> E -> C [the same C as earlier]  
Output:   C

## Leetcode ##
[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/#/description)
[Linked List Cycle 2](https://leetcode.com/problems/linked-list-cycle-ii/#/description)

[circular]: ./circular-linked-list.png