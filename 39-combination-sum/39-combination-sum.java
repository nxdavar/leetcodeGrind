class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> temp = new ArrayList<Integer>();
        helper(res, temp, candidates, target, 0, 0);
        return res;
    }
    public void helper(List<List<Integer>> res, List<Integer> temp, int[] candidates, int target, int curr, int start) {
        if(curr <= target) {
            if(curr == target) {
                List<Integer> toAdd = new ArrayList<Integer>();
                for(int i = 0; i < temp.size(); i++) {
                    toAdd.add(temp.get(i));
                }
                res.add(toAdd);
                return;
            }
            // iterate through choices:
            for(int i = start; i < candidates.length; i++) {
                temp.add(candidates[i]);
                curr += candidates[i];
                helper(res, temp, candidates, target, curr, i);
                temp.remove(temp.size() - 1);
                curr -= candidates[i];
            } 
        }
    }
}