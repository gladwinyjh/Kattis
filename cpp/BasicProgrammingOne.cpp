#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n, t, input;
    vector<int> A;

    cin >> n >> t;

    for (int i=0; i<n; i++) {
        cin >> input;
        A.push_back(input);
    }

    if (t == 1) {
        cout << 7 << endl;
    } else if (t == 2) {
        if (A[0] > A[1]) {
            cout << "Bigger" << endl;
        } else if (A[0] == A[1]) {
            cout << "Equal" << endl;
        } else {
            cout << "Smaller" << endl;
        }
    } else if (t == 3) {
        // // Sort and take A[1]
        sort(A.begin(), A.begin()+3);
        cout << A[1] << endl;
    } else if (t == 4) {
        // int range too small; put long
        long sum = 0;
        for (auto& i : A) {
            sum += i;
        }
        cout << sum << endl;   
    } else if (t == 5) {
        // int range too small; put long
        long sum = 0;
        for (auto& i : A) {
            if (i%2==0) {
                sum += i;
            }
        }
        cout << sum << endl;
    } else if (t == 6) {
        for (auto& i : A) {
            cout << "abcdefghijklmnopqrstuvwxyz"[i%26];
        }
    } else {
        int i = 0;
        // visited vector to check for infinite loop
        vector<bool> visited(n, false);

        while (true) {
            i = A[i];

            // Don't need to check i < 0 as values are non-negative
            if (i > n-1) {
                cout << "Out" << endl;
                break;
            } else if (i == n-1) {
                cout << "Done" << endl;
                break;
            } 

            if (visited[i]) {
                cout << "Cyclic" << endl;
                break;
            }
            // Set index as visited
            visited[i] = true;
        }
    }
}