/*
 * =====================================================================================
 *
 *       Filename:  Pascal's Triangle.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  09/11/2013 20:43:36
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Lu, 
 *        Company:  
 *
 * =====================================================================================
 */
class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector <vector < int >> ans;
        ans.clear();
        if  (numRows == 0)return ans;
        vector < int > row;
        row.clear();
        row.push_back(1);
        ans.push_back(row);
        int c = 1;
        for (int i = 1 ; i < numRows ; i ++){
            c ++;
            row.clear();
            row.push_back( 1 );
            for (int j = 1 ; j < c - 1 ; j ++){
                row.push_back( ans[i-1][j-1] + ans[i-1][j] );
            }
            row.push_back( 1 );
            ans.push_back(row);
        }
        return ans;
    }
};
