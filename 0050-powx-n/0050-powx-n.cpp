class Solution {
public:
    double myPow(double x, int n) {
        if (x == 0) return 0;
        if (x == 1) return 1;
        if (x == -1)
        {
            if (n % 2 == 0) return 1;
            return -1;
        } 
        
        if (n == 0) return 1;
        double res = 1, curr = x;
        bool neg = n < 0, min = n == INT_MIN;
        if (min) ++n;
        if (neg) n *= -1;
        while(n > 0)
        {
            if (n % 2 == 1)
            {
                res *= curr;
            }
            n /= 2;
            curr *= curr;
        }
        if (neg) res = 1/res;
        if (min) res /= x;
        return res;
    }
};