class Solution {
public:
    int integerBreak(int n) {
        if(n == 2) return 1;
        if(n == 3) return 2;
        int *num = new int[n];
        for(int i = 0;i < n;i++) num[i] = 0;
        num[1] = 2; num[2] = 3;
        for(int i = 3;i < n;i++){
            num[i] = max(num[i-2] * 2, num[i-3] * 3); 
        }
        return num[n-1];
    }
};