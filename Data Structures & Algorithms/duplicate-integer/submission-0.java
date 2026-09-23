class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            map.merge(nums[i], 1, Integer::sum);
            if(map.get(nums[i]) > 1){
                return true;
            }
        }
        return false;
    }
}
