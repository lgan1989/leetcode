class Solution {
public:
    void setZeroes(vector<vector<int> > &matrix) {
        int m = matrix.size();
        if (m == 0)return;
        int n = matrix[0].size();
        if (n == 0)return;
        int r , c;
        r = c = matrix[0][0];

		for (int i = 0 ; i < n ; i ++)
			if (matrix[0][i] == 0)r = 0;
        for (int i = 0 ; i < m ; i ++)
            if (matrix[i][0] == 0)c = 0;
		int e = r == 0 ? r : c;

        for (int i = 0 ; i < m ; i ++){
            bool flag = false;
            for (int j = 0 ; j < n ; j ++){
                if (matrix[i][j] == 0){
                    flag = true;
                }
            }
            if (flag){
                matrix[i][0] = 0;
            }
        }


        for (int i = 0 ; i < n ; i ++){
            bool flag = false;

            for (int j = 0 ; j < m ; j ++){

                if (matrix[j][i] == 0){
                    flag = true;
                }
            }
            if (flag){
                matrix[0][i] = 0;
            }
        }

        for (int i = m-1 ; i >= 0 ; i --){
            for (int j = n-1 ; j >= 0 ; j --){

                if (i == 0){
					if (r == 0)
						matrix[i][j] = 0;
                    continue;
                }
                if (j == 0){
					if (c == 0)
						matrix[i][j] = 0;
                    continue;
                }
                if ( matrix[i][0] == 0 || matrix[0][j] == 0){
                    matrix[i][j] = 0;
                }
            }
        }
		matrix[0][0] = e;
    }
};
