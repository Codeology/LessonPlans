[<- Back to question](../questions/question-sum-lists.md)

## Sample Code ##
[Java](./java-sum-lists.java)

## Ideas ##

Important to sum while in the linked list form and not convert
both input lists to integers first because if you convert first,
THEN add, you may run into integer overflow problems and will
have to account for that. If you keep them in the linked list
form and add one digit at a time, you'll never encounter an
integer overflow problem by adding `9` and `9` (the max digits).

On top of the integer overflow reason, you can also overwrite
one of the linked lists as you're adding, effectively using `O(1)`
space. Time complexity is bound by the time needed to run through
the longest linked list once, so `O(n)`.