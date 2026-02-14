class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] res = new int[nums.length];
        int i = 0;
        int j = n;
        int k = 0;
        while (i < n) {
            res[k++] = nums[i++];
            res[k++] = nums[j++];
        }
        
        return res;
    }
}