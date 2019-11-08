#define pov_max pow(2,32)-1
#define nev_max pow(2,32)*-1
class Solution {
public:
    int reverse(long long int x) {
        long long int rev = 0;
        bool nev = false;
        long int maxx;
        if (x < 0){
            maxx = INT_MIN;
            maxx *= -1;
            x *= -1;
            nev = true;
        }
        else maxx = INT_MAX;
        while(x > 0){
            rev = rev*10 + x%10;
            if (rev >= maxx ) return 0;
            x /= 10;
        }
        if (nev)
            return -rev;
        return rev;
    }
};