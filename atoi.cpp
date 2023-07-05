#include <bits/stdc++.h> 
int atoi(int ind, int ans, string& str) {
    
    if (ind == str.size()) {
        return ans;
    }
    if ('0' <= str[ind] && str[ind] <= '9') {
 
        return atoi(ind + 1, 10 * ans + str[ind] - '0', str);
    } else {
        return atoi(ind + 1, ans, str);
    }
}

int atoi(string str) {
    int num = atoi(0, 0, str); 
    if (str[0] == '-') {
        num *= -1;
    }
    return num;
}