[<- Back to question](../questions/question-loop-detection.md)

## Sample Code ##
[Python](./python-loop-detection.py)

## Ideas ##

So we want to detect whether there is a cycle in the linked list. We
can see that if we use one pointer and simply iterate down the nodes,
we don't have the right tools for detecting when we've started cycling.

How about introducing some memory? We can add into a hashset all the
nodes we've seen before, and check if the current node we're about
to visit has been seen. If it has, then that node must be the start
of the cycle. This approach would have to visit all the unique nodes
in the linked list and will store as much, so both the runtime and
space complexity are linear, aka `O(n)`.

What if our nodes pack a lot of information, or if the list is really
really long? Can we optimize our current approach? Can we save either
space or runtime here? We just want to find whether a cycle exists,
so specific nodes don't really matter.

Let's try the classic "tortoise and hare" technique, a.k.a the "runner"
technique. The idea is that when we're working with circular linked
lists, if we have one pointer traveling faster than another pointer,
the faster pointer will eventually overlap the slower pointer. By using
this technique, we don't need to store all the nodes we've seen
in order to do a cross check. We simply keep iterating until the
pointers are referencing the same node, meaning we've entered a cycle
OR until the faster pointer
hits the end of the linked list, meaning the list wasn't circular
to begin with. Our new algorithm reduces the space complexity of
the solution to `O(1)` and our runtime stays linear. To see that the
runtime is still linear, think about what the worst-case amount of
work you're doing is. In the worst case, the runner will catch up
to the normal pointer somewhere before the second lap around the
cycle. So how long is the cycle? In the worst case, the last node of
the linked list loops back to the first node. So overall, the most
you'll iterate is `O(2n)`, which is still linear.

Now.. what if we wanted to actually return the node at the beginning
of the cycle?
