unordered_map < string , int> toRemove;
unordered_set < int > pre[10010];
vector < vector < string > > result;

struct ele{
    string word;
	int dis;
};

ele q[1000010];

void findResult(int pos , vector < string > tmp){

	if (pos == 0){
		tmp.insert(tmp.begin() , q[pos].word);
		result.push_back(tmp);
		return;
	}
	tmp.insert(tmp.begin() , q[pos].word);
	for (auto it = pre[pos].begin() ; it != pre[pos].end() ; it ++){
		int p = *it;	
		findResult(p , tmp);
	}
}

class Solution {
public:
	vector<vector<string>> findLadders(string start, string end, unordered_set<string> &dict) {
		
		toRemove.clear();
		result.clear();
		int head = 0 , tail = 0;
		ele tmp;
		tmp.word = start;
		tmp.dis = 1;
		dict.insert(end);
		for (int i = 0 ; i < 10000 ; i ++)pre[i].clear();
		q[head ++] = tmp;
		int depth = 0;
		toRemove[start] = 0;
		int wordLen = start.length();
		while (head != tail){
			tmp = q[tail ++];
			if (tmp.word == end){
				vector < string > vec;
				vec.clear();
				findResult(tail - 1 , vec);
				return result;
			}
			if (tmp.dis > depth){
				depth = tmp.dis;
				for (auto it = toRemove.begin() ; it != toRemove.end() ; it ++){
					dict.erase((*it).first);
				}
				toRemove.clear();
			}
			for (int i = 0 ; i < wordLen ; i ++){
				for (int c = 'a' ; c <= 'z' ; c ++){
					string w = tmp.word;
					w[i] = c;
					if (w == tmp.word)continue;
					if (dict.count(w)){
									
						ele nx;
						nx.word = w;
						nx.dis = tmp.dis + 1;

						if (toRemove.count(w) == 0){
							toRemove[w] = head;
							pre[head].insert(tail - 1);
							q[head ++] = nx;
						}
						else{
							pre[ toRemove[w] ].insert(tail - 1);
						}
					}
				}
			}
		}

		return result;
	}
	
};

