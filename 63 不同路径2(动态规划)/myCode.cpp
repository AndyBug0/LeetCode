class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        const int m = obstacleGrid.size();
        const int n = obstacleGrid[0].size();
        int *path = new int[n];
        for(int i = 1;i < n;i++) path[i] = 0;
        path[0] = obstacleGrid[0][0] == 0? 1 : 0;
        for(int i = 0;i < m;i++){
            for(int j = 0;j < n;j++){
                path[j] = obstacleGrid[i][j]? 0 : j == 0 ? path[j] : path[j-1] + path[j];
            }
        }
        return path[n-1];
    }
};