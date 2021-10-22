#include <unordered_map>
#include <iostream>

using namespace std;

int main(){
    // Unordered maps to store entries of both systems
    unordered_map<string, int> systemOne;
    unordered_map<string, int> systemTwo;
    int n;

    cin >> n;

    for (int i=0; i<2; i++) {
        for (int j=0; j<n; j++) {
            string a;
            cin >> a;
            
            if (i==0) {
                // Store in first map
                systemOne[a] ++;
            } else {
                // Store in second map
                systemTwo[a] ++;
            }     
        }
    }

    int count = 0;
    for (const auto& answer: systemOne) {
        // If both maps systems have the same key
        if (systemTwo.count(answer.first) != 0) {
            // Increment count by the minimum of values from both maps
            // Min value indicates the max possible matches for that key
            count += min(answer.second, systemTwo[answer.first]);
        }
    }
    cout << count << endl;
}