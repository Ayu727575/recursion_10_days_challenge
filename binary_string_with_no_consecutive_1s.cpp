void solve(vector<string> &vec, int pos, int k, string s){
    if(pos == k){
        vec.push_back(s);
        return;
    }
    if(pos==0){
        solve(vec, pos+1, k, s+"0");
        solve(vec, pos+1, k, s+"1");
    }
    else{
        solve(vec, pos+1, k, s+"0");
        if(s.back()=='0'){
            solve(vec, pos+1,k,s+"1");
        }
    }
}
vector<string> generateString(int N) {
    // Write your code here.
    vector<string> vec;
    solve(vec, 0, N, "");
    return vec;
}