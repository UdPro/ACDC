class Solution {
public:
    bool isValid(string s) {
    stack <char> st;
    for ( int i= 0 ; i < s.length() ; i++){
        if ( s[i] == '[' or s[i] == '(' or s[i] == '{'){
            st.push(s[i]);
            continue;
        }
        else if ( s[i] == ')' && (st.size() == 0 || st.top() != '(') )
            return false;
        else if ( s[i] == ']' && (st.size() == 0 || st.top() != '[') )
            return false;
        else if ( s[i] == '}' && (st.size() == 0 || st.top() != '{') )
            return false;
        st.pop();
        cout << st.size() << endl;
    }
    if (st.size() == 0)
        return true;
    return false;
    }
};