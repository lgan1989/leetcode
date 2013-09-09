map < int , int > pos;

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int len = numbers.size();
        vector < int > ret;
        ret.clear();
        pos.clear();
        for (int i = 0 ; i < len ; i ++)pos[numbers[i]] = i + 1;
        for (int i = 0 ; i < len ; i ++){
            int idx = pos[target - numbers[i]];
            if (idx){
                ret.push_back(min(idx , i + 1));
                ret.push_back(max(idx , i + 1));
                return ret;
            }
        }
    }
};

