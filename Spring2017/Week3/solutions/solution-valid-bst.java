    public boolean isValidBST(TreeNode root) {
        return valid(root, (long) Integer.MIN_VALUE-1, (long) Integer.MAX_VALUE+1);
    }
    private boolean valid(TreeNode root, long min, long max) {
        if (root == null) return true;
        if (root.val <= min || root.val >= max) return false;
        return valid(root.left, min, root.val) && valid(root.right, root.val, max);
    }
