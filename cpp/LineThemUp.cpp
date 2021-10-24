#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n;
    string name;
    vector<string> lineUp;
    

    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> name;
        lineUp.push_back(name);
    }

    vector<string> ascendingLineUp(lineUp.size());
    vector<string> descendingLineUp(lineUp.size());

    partial_sort_copy(lineUp.begin(), lineUp.end(), ascendingLineUp.begin(), ascendingLineUp.end());
    partial_sort_copy(lineUp.begin(), lineUp.end(), descendingLineUp.begin(), descendingLineUp.end(), greater<string>());

    if (lineUp == ascendingLineUp) {
        cout << "INCREASING" << endl;
    } else if (lineUp == descendingLineUp) {
        cout << "DECREASING" << endl;
    } else {
        cout << "NEITHER" << endl;
    }
}