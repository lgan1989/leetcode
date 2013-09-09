bool visited[3100][3100];

int r , c;
int depth;
int dir[4][2] = {0 , 1 , 1 , 0 , 0 , -1 , -1 , 0};

typedef pair<int,int> intpair;

stack < pair<int , int> > myStack;

class Solution {
public:
    void flip(intpair pos , char x , vector<vector<char>> &board){

		if (visited[pos.first][pos.second])return;
		if (board[pos.first][pos.second] == 'X')return;
		
		myStack.push( pos );
		while (!myStack.empty())
		{
			intpair loc = myStack.top();
			board[loc.first][loc.second] = x;
			visited[loc.first][loc.second] = 1;
			myStack.pop();
			for (int i = 0 ; i < 4 ; i ++){

				int ni = loc.first + dir[i][0];
				int nj = loc.second + dir[i][1];
				if ( ni < 0 || nj < 0 || ni >= r || nj >= c )continue;
				if ( board[ni][nj] == 'X')continue;
				if ( visited[ni][nj] )continue;
				board[ni][nj] = x;
				myStack.push( intpair(ni , nj) );

			}

		}
		
	

	}
	void solve(vector<vector<char>> &board) {
		// Start typing your C/C++ solution below
		// DO NOT write int main() function

		r = board.size();
		if (r == 0)return;
		c = board[0].size();

		while (!myStack.empty())myStack.pop();

		memset(visited , 0 , sizeof(visited));

		for (int i = 0 ; i < r ; i ++){
			flip(intpair(i , 0) , 'O' , board);
			flip(intpair(i , c - 1) , 'O' , board);

		}
		for (int i = 0 ; i < c ; i ++){
			flip(intpair(0 , i) , 'O' , board);
			flip(intpair(r - 1 , i) , 'O' , board);
		}
		for (int i = 0 ; i < r ; i ++)
			for (int j = 0 ; j < c ; j ++)
				flip(intpair(i , j) , 'X' , board);
	}
};

