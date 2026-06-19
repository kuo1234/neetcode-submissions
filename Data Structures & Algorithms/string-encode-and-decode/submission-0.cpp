#include <iostream>
#include <cstdio>
#include <vector>
#include <unordered_map>
#include <cstring>
using namespace std;

class Solution {
public:

    string encode(vector<string>& strs) {
        for(int i=0;i<strs.size();i++){
            strs[i] = to_string(strs[i].size()) + "#" + strs[i];
        }
        string result = "";
        for(const string& s : strs) {
            result += s;
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (j < s.length() && s[j] != '#') {
                j++;
            }
            int len = stoi(s.substr(i, j - i));
            result.push_back(s.substr(j + 1, len));
            i = j + 1 + len;
        }
        return result;
    }
};