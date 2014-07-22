/*
 * =====================================================================================
 *
 *       Filename:  Pascal's Triangle II.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  09/11/2013 20:48:14
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
    vector<int> getRow(int rowIndex) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector < int > row;
        vector < int > last;
        row.clear();
        last.clear();
        last.push_back(1);
        int c = 1;
        for (int i = 1 ; i <= rowIndex ; i ++){
            c ++;
            row.clear();
            row.push_back( 1 );
            for (int j = 1 ; j < c - 1 ; j ++){
                row.push_back( last[j-1] + last[j] );
            }
            row.push_back( 1 );
            last = row;
        }
        return last;       
    }
};


