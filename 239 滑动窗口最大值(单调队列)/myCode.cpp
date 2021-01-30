class Solution {
public:
    class MyQueue{
    private:
        deque<int> que;
    public:
        void push(int val){
            while(!que.empty() && que.back() < val){
                que.pop_back();
            }
            que.push_back(val);
        }
        void pop(int val){
            if(val == que.front())
                que.pop_front();
        }
        int front(){
            return que.front();
        }
    };
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        MyQueue queue;
        vector<int> result;
        for(int i = 0;i < k;i++){
            queue.push(nums[i]);
        }
        result.push_back(queue.front());
        for(int i = k;i < nums.size();i++){
            queue.pop(nums[i-k]);
            queue.push(nums[i]);
            result.push_back(queue.front());
        }
        return result;
    }
};