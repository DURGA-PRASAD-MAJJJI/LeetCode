import java.util.*;

class Solution {
    public int[] findErrorNums(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] res = new int[2];
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        for (int key : map.keySet()) {
            if (map.get(key) > 1) {
                res[0] = key;
                break;
            }
        }
        for (int i = 1; i <= nums.length; i++) {
            if (!map.containsKey(i)) {
                res[1] = i;
                break;
            }
        }
        return res;
    }
}
