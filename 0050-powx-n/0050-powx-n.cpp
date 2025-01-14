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

        // Much more elegant
        double res = 1;
        if (n == INT_MIN) 
        {
            ++n; 
            res /= x;
        }
        
        if (n < 0)
        {
            x = 1/x;
            n = -n;
        }

        double curr = x;

        while(n > 0)
        {
            if (n % 2 == 1)
            {
                res *= curr;
            }
            n /= 2;
            curr *= curr;
        }
       
        return res;
    }
};