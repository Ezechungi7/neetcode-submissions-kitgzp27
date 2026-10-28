class Solution {
public:
    bool canJump(vector<int>& nums) {
        
   int gas = 0;
        for(int n : nums) {
            if(gas < 0) return false;
            if(n > gas) gas = n;
            gas -= 1;
        }
        return true;
    }
};