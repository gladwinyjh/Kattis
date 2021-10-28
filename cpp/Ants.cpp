#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t, l, n;

    cin >> t;

    for (int i=0; i<t; i++) {
        cin >> l >> n;
        vector<int> pos(n);

        for (auto& j: pos) {
            cin >> j;
        }

        int earliest = 0, latest = 0;

        for (auto& j : pos) {
            if (j > l-j) {
                earliest = max(earliest, l-j);
                latest = max(latest, j);
            } else {
                earliest = max(earliest, j);
                latest = max(latest, l-j);
            }
        }
        cout << earliest << " " << latest << endl;
    }
}