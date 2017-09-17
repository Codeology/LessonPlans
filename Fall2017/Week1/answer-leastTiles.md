### Ideas

There are a couple of tricky things that I didn't notice the first time around,
and it caused me some trouble:
* only tiles that are the same number will merge
* only tiles that are _neighbors_ OR are separated only by `0`s will merge

After realizing these two points and really looking at a sample input/output,
a brute force solution immediately came to mind. First, find all the possible
merges that doing an up/down move will give me. Then find all the possible
merges that doing a left/right move will give me. Compare those two totals
and output `0`, `1`, or `2` depending on which one is bigger.

### Code

Here's some sample code: [leastTiles.py](./leastTiles.py) [leastTiles.java](./leastTiles.java)

### Runtime and Space Complexity

If the input is width (n) x height (m), then the runtime of the above solution
is `O(n*m)`. We do `O(n)` work for each row in the tile matrix, and we do that `m`
times.

The space complexity is constant or `O(1)` since we don't allocate any extra
space.
