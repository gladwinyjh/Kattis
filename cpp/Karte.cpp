#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    string input;
    cin >> input;

    // Keep track of repeated cards
    unordered_map<string, int> map;
    // Keep track of quantity of missing cards of each suit
    unordered_map<char, int> quantityMissing = 
    {
        {'P', 13},
        {'K', 13},
        {'H', 13},
        {'T', 13}
    };
    

    for (int i=0; i<input.length(); i+=3) {
        string TXY = input.substr(i,3);

        if (map.count(TXY) == 0) {
            // Add card to map
            map[TXY] ++;
        } else {
            // Card is repeated
            cout << "GRESKA" << endl;
            return 0;
        }

        // One less card missing from suit
        quantityMissing[TXY[0]] --;
    }

    cout << quantityMissing['P'] << " ";
    cout << quantityMissing['K'] << " ";
    cout << quantityMissing['H'] << " ";
    cout << quantityMissing['T'] << endl;
}