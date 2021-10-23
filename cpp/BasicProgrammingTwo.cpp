#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main(){
    int n, t, input;
    vector<int> A;
    unordered_map<int, int> map;

    cin >> n >> t;

    for (int i=0; i<n; i++) {
        cin >> input;
        A.push_back(input);
        map[input] ++;
    }

    if (t == 1) {
        for (const auto& i : A) {
            if (map[7777 - i] && i != map[7777 - i]) {
                cout << "Yes" << endl;
                return 0;
            }
        }
        cout << "No" << endl;
    } else if (t == 2) {
        for (const auto& val : map) {
            // Frequency of value more than 1
            if (val.second > 1) {
                cout << "Contains duplicate" << endl;
                return 0;
            }
        }
        cout << "Unique" << endl;
    } else if (t == 3) {
        for (const auto& val : map) {
            // Frequency > N/2
            if (val.second > n/2) {
                cout << val.first << endl;
                return 0;
            }
        }
        cout << -1 << endl;
    } else if (t == 4) {
        // Sort before getting median
        sort(A.begin(), A.end());

        if (n % 2 == 0) {
            cout << A[n/2 - 1] << " " << A[n/2] << endl;
        } else {
            cout << A[n/2] << endl;
        }
    } else {
        // Sort first
        sort(A.begin(), A.end());

        for (const auto& val : A) {
            if (val >= 100 && val <= 999) {
                cout << val << " ";
            }
        }
    }
}