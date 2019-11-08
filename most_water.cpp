class Solution {
public:
    int maxArea(vector<int>& height) {
        int m =0;
        int lo, hi;
        lo = 0;
        hi = height.size() -1 ;
        while( lo < hi){
            m = max(m,min(height[lo],height[hi])*(hi-lo));
            if (height[lo] < height[hi] )
                lo++;
            else
                hi--;
        }
        return m;   
    }
};