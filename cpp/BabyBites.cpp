#include <iostream>
#include <string> 
#include <vector> 

using namespace std;

#define pb push_back


int main(){
    int n;
    string a;
    vector <string> numbers;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a;
        numbers.pb(a);
    }

    int count = 1;
    for (int i = 1; i <= numbers.size(); i++) {
        // String is mismatched and baby did not say "mumble"
        if (to_string(i) != numbers[i-1] && numbers[i-1] != "mumble") {
            cout << "something is fishy" << endl;
            return 0;
        }
    }
    cout << "makes sense" << endl;
}