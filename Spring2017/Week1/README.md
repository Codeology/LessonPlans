## Lesson

**Lists** allow you to have an extendable collectoin of indexed variables.
Indexing is awesome because you can access any element you want in constant
time if you know which location it's in.

**Strings** are like lists of
characters, except they're immutable, which means that trying to change 
even one character in a string will cause the computer to rewrite the whole
string in memory. Use lists of characters if you need to modify the string,
i.e.

`characters = list("mystring")` or `"mystring".split()`

**Dictionaries** are like lists, except instead of numbers, the indexes
can be anything. They're also called _keys_ instead of _indexes_. Finding
out whether a key exists in a dictionary takes constant time, whereas
finding out whether an element exists in a list takes linear time.

## Demo

Write a function to output the duplicate characters in a string.

## Mock Interview Questions

* [(Easy) First unique character in a string](./question-firstUniqueCharacterinString.md) | [solution](./answer-firstUniqueCharacterinString.md)
* [(Medium) Least Tiles](./leastTiles.md) | [solution](./answer-leastTiles.md)
