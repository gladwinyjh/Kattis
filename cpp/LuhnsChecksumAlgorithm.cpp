#include <iostream>
#include <string>

using namespace std;

int main(){
    int n;

    cin >> n;

    for (int i=0; i<n; i++) {
        int total = 0;
        string number;
        cin >> number;

        // Current index from back
        int j = number.size()-1;
        // Flag for every second digit
        bool second = false;
        while (j >= 0) {
            if (!second) {
                // Increment total by int of number[j]
                total += number[j] - '0';
                second = true;
            } else {
                // 2 * int of number[j]
                int d = 2 * (number[j] - '0');
                if (d > 9) {
                    // Add first and second digit together
                    d = d/10 + d%10;
                }
                total += d;
                second = false;
            }
            // Go backwards
            j--;
        }

        if (total % 10 == 0) {
            cout << "PASS" << endl;
        } else {
            cout << "FAIL" << endl;
        }
    }
}