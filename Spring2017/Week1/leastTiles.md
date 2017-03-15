2048 is an addictive game that you've probably seen already.
The game is played on a rectangular field that consists of
`tiles` that are either empty or filled with numbers, where each
number is a power of `2`. The player uses the arrow keys to move
all the tiles in one direction per key press: up, down, left,
or right. When two tiles with the same number collide after a
move, they merge into one tile, and the number written on the
new tile is twice as large as the number written on each of
the original tiles.

In this challenge, you are given `tiles` representing a state
of the game. The task is to write an algorithm that determines
which arrow key should be pressed next such that the smallest
possible amount of tiles with numbers on them remain after the
move.

Return 1 if the _up_ or _down_ key should be pressed,
2 if the _right_ or _left_ key should be pressed,
and 0 if _any_ key can be pressed.

#### Example
```python
tiles = [[2,4,16,8],
         [0,4,8,0],
         [0,0,0,0],
         [0,0,2,0]]
```

the output should be

`leastTiles(tiles) = 1`

Pressing the _up_ or _down_ key will merge two 4s into one tile with the number 8. Pressing _left_ or _right_ won't result in any merges. Thus, the answer is `1`.
