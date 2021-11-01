#include <iostream>

using namespace std;

int main(){
    int k;

    cin >> k;

    while (k > 0) {
        int n;
        cin >> n;

        // Minimum number of pushes to top of dvd stack is 1 for each incorrectly placed dvd
        // Go through input and find number of dvds that are not perfectly increasing.
        int next = 1; // Next dvd number in stack
        for (int i=0; i<n; i++) {
            int dvd;
            cin >> dvd;

            if (dvd == next) {
                next ++;
            }
        }
        // +1 to offset next ++ for the last.
        cout << n-next+1 << endl;
        k --;
    }
}
