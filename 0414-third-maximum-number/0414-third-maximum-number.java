import java.util.*;

class Solution {
    public int thirdMax(int[] nums) {
        Map<Integer, Integer> map = new LinkedHashMap<>();
        ArrayList<Integer> r = new ArrayList<>();
        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            r.add(entry.getKey());
        }
        Collections.sort(r);
        if (r.size() < 3) {
            return r.get(r.size() - 1);   // return maximum
        }
        return r.get(r.size() - 3);
    }
}
