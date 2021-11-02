#include <iostream>
#include <unordered_map>

using namespace std;

// Map to store number and values
unordered_map<char, pair<int, int>> map = 
    {
        {'A', {11,11}},
        {'K', {4,4}},
        {'Q', {3,3}},
        {'J', {20,2}},
        {'T', {10,10}},
        {'9', {14,0}},
        {'8', {0,0}},
        {'7', {0,0}}
    };

int main() {
    int N;
    char B;
    int sum = 0;

    cin >> N >> B;

    for (int i=0; i<4*N; i++) { // End when i < Number of hands * 4 (number of cards in a hand)
        string s;
        cin >> s;

        if (s[1] == B) { // Current suit is dominant
            sum += map[s[0]].first; // Add the dominant value
        } else { // Current suit is not dominant
            sum += map[s[0]].second; // Add the non-dominant value
        }
    }

    cout << sum << endl;
}