
### Ideas

Something we care about with this problem is character counts. When I
see that I need to _count_ everything in an input, I immediately think
about **dictionaries**. 

A very common use of dictionaries is to produce this kind of count:

```python
string = "helloworld"
counts = {} # initalize an empty dictionary
for char in string:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

# counts = { 'h': 1,
#            'e': 1,
#            'l': 3,
#            'o': 2,
#            'w': 1,
#            'r': 1,
#            'd': 1 }
```

In general, this pattern of using dictionaries is to collect frequencies
in an efficient way. We can use this idea to collect the frequency of
each character in the input string, and then interate once more through
the string to find the first character that is unique.

### Code

Here's some sample Python code: [firstUniqueCharacterInString.py](./firstUniqueCharacterInString.py)

#### (Bonus)

A pythonic way to create the `counts` dictionary is to use the built-in
`count` method on Python arrays:

`counts = {char: string.count(char) for char in string}`

### Runtime and Space Complexity

This solution runs in `O(n)` time. It takes `O(n)` to create the frequency
dictionary, and another `O(n)` to go through the string and find the 
index of the unique character.

The space complexity here is `O(n)`. We are storing up to `n` items in the
dictionary.

### Other resources

* [Java solution](https://discuss.leetcode.com/topic/55148/java-7-lines-solution-29ms)
* [Python: What is `enumerate`?](https://docs.python.org/2/library/functions.html#enumerate)
* [Python: list comprehension](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
* [Python: Dictionary comprehension](http://stackoverflow.com/questions/1747817/create-a-dictionary-with-list-comprehension-in-python)
