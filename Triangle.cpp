/*
 * =====================================================================================
 *
 *       Filename:  Triangle.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  09/11/2013 20:18:32
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Lu, 
 *        Company:  
 *
 * =====================================================================================
 */

int f[100010][2];

class Solution {
public:
    int minimumTotal(vector<vector<int> > &triangle) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int r = triangle.size();
        int flag = 0;
        if (r == 0)return 0;
        f[0][flag] = triangle[0][0];
      
        for (int i = 1 ; i < r ; i ++){
            int c = triangle[i].size();
            flag = 1 - flag;
            f[0][flag] = f[0][1-flag] + triangle[i][0];
            f[c-1][flag] = f[c-2][1-flag] + triangle[i][c-1];
            for (int j = 1 ; j < c - 1 ; j ++){
           
                f[j][flag] = min(f[j - 1][1-flag] + triangle[i][j] , f[j][1-flag] + triangle[i][j]);
             
            }
        }
        int ans = INT_MAX;
        for (int i = 0 ; i < triangle[r-1].size(); i ++){
            ans = min(ans , f[i][flag]);
        }
        return ans;
    }
};
