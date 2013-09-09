
struct ele{
	int dis;
	string word;
};

queue < ele > q;

class Solution {
public:
	int ladderLength(string start, string end, unordered_set<string> &dict) {
		// Start typing your C/C++ solution below
		// DO NOT write int main() function 
		ele tmp;
		tmp.dis = 1;
		tmp.word = start;
		while (!q.empty())q.pop();
		q.push(tmp);
		dict.erase(start);
		while (!q.empty()){
			tmp = q.front();
			q.pop();
			if (tmp.word == end){
				return tmp.dis;
			}
			int l = tmp.word.size();
			for (int i = 0 ; i < l ; i ++){
				string nx = tmp.word;
				for (int j = 'a' ; j <= 'z' ; j ++){
					nx[i] = j;
					ele next;
					next.word = nx;
					next.dis = tmp.dis + 1;
					if (dict.count(nx)){
						dict.erase(nx);
						q.push(next);
					}
				}
			}
		}


		return 0;

	}
};