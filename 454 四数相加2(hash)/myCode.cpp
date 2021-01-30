class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int,int> mapAB;
        for(int i = 0;i < A.size();i++){
            for(int j = 0;j < B.size();j++){
                auto iter = mapAB.find(A[i]+B[j]);
                if(iter != mapAB.end()){
                    iter->second++;                    
                }
                else{
                    mapAB[A[i]+B[j]] = 1;
                }
            }
        }
        int ans = 0;
        for(int i = 0;i < A.size();i++){
            for(int j = 0;j < B.size();j++){
                auto iter = mapAB.find(0-C[i]-D[j]);
                if(iter != mapAB.end()){
                    ans += iter->second;
                }
            }
        }
        return ans;
    }
};