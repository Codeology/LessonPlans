## Lesson

In a general software engineering interview, learning how to work with strings,
arrays, and dictionaries is a great way to break your logic down into parts
and make sure it's robust. You'll use "control flow" tools like `for` loops,
`while` loops, and `if`/`else` statements a lot. You'll also have to be careful
of off-by-one errors. The higher mastery you have with the array and dictionary
data structures, and the algorithms involved with manipulating them, the 
better you will be able to demonstrate control flow logic.

**Arrays** allow you to have an extendable collection of indexed variables.
Indexing is awesome because you can access any element you want in constant
time if you know which location it's in.

```python
arr = ['h','e','l','l','o']
print(arr[0]) # 'h'
print(arr[-1]) # 'o'
print(arr[1:3]) # ['e', 'l']
```

**Strings** are like arrays of
characters, except they're immutable, which means that trying to change 
even one character in a string will cause the computer to rewrite the whole
string in memory. Use arrays of characters if you need to modify the string,
i.e.

```python
characters = list("mystring") # or "mystring".split()
characters[5] = "o"
print "".join(characters) # "mystrong"
```

**Dictionaries** are like arrays, except instead of numbers, the _indexes_
can be anything. They're also called _keys_ instead of _indexes_. Finding
out whether a key exists in a dictionary takes constant time, whereas
finding out whether an element exists in an array takes linear time.

```python
d = {}
d['foo'] = 'bar'
print('baz' in d) # constant time check due to hashing

counts = {}
counts['a'] = 1
counts['a'] += 1
counts['b'] = 1

print(counts) # {'b': 1, 'a': 2} note that dictionaries may not preserve order
```

## Demo

Write a function to output the duplicate characters in a string.

Thought process:

1. sample inputs / outputs (ask questions to clarify, if needed)
2. test cases + edge cases
3. write the code
4. test the code

## Mock Interview Questions (work in pairs or on your own time, we'll review some together)

* [(Easy) Search Insert Position (leetcode)](https://leetcode.com/problems/search-insert-position/#/description)
* [(Easy) Plus One (leetcode)](https://leetcode.com/problems/plus-one/#/description)
* [(Easy) First unique character in a string](./question-firstUniqueCharacterinString.md) | [solution](./answer-firstUniqueCharacterinString.md)
* [(Easy) Majority Element (leetcode)](https://leetcode.com/problems/majority-element/#/description)
* [(Easy) Two Sum (leetcode)](https://leetcode.com/problems/two-sum/#/description)
* [(Medium) 3 Sum (leetcode)](https://leetcode.com/problems/3sum/#/description)
* [(Medium) Compare Version Numbers (leetcode)](https://leetcode.com/problems/compare-version-numbers/#/description)
* [(Medium) Least Tiles](./leastTiles.md) | [solution](./answer-leastTiles.md)
* [(Medium) Group Anagrams (leetcode)](https://leetcode.com/problems/anagrams/#/description) | [solutions](https://discuss.leetcode.com/category/57/anagrams)
* [(Medium) All permutations (GeeksForGeeks)](http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/)
* [(Hard) Median of Two Sorted Arrays (leetcode)](https://leetcode.com/problems/median-of-two-sorted-arrays/#/description)
* [(Hard) Longest Consecutive Sequence (leetcode)](https://leetcode.com/problems/longest-consecutive-sequence/#/description)
