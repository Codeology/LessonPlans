// 1 if up or down, 2 if left or right, 0 if either one
public int leastTiles(int[][] tiles) {
	// Good Practice to ask for error handling
	int vertical = verticalCount(tiles);
	int horizontal = horizontalCount(tiles);
	int diff = vertical - horizontal;
	if (diff==0) return 0;
	return diff > 0 ? 1 : 2; 
}

private int verticalCount(int[][] tiles) {
	int count = 0, pre, cur;
	for (int i=0; i<tiles[0].length; i++) {
		pre = tiles[0][i];
		for (int j=1; j<tiles.length; j++) {
			cur = tiles[j][i];
			if (cur == 0) continue; 
			if (pre == cur) {
				pre = -1;
				count++;
			} else {
				pre = cur;
			}
		}
	}
	return count;
}

private int horizontalCount(int[][] tiles) {
	int count = 0, pre, cur;
	for (int i=0; i<tiles.length; i++) {
		pre = tiles[i][0];
		for (int j=1; j<tiles[0].length; j++) {
			cur = tiles[i][j];
			if (cur == 0) continue; 
			if (pre == cur) {
				pre = -1;
				count++;
			} else {
				pre = cur;
			}
		}
	}
	return count;
}