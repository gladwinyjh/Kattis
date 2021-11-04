#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    string word;

    cin >> n >> word;

    // Store initial arrangement as oldDeck, and a copy to be altered as currDeck
    // Each element at an index given by its unique index number 
    vector<int> oldDeck(n), currDeck(n);
    for (int i=0; i<n; i++) {
        oldDeck[i] = i;
        currDeck[i] = i;
    }

    // Vector for left and right card piles
    vector<int> left, right;
    int shuffles = 0;
    do {
        shuffles ++;

        if (n%2 == 0) { // Even number of cards (Same arrangement for in and out shuffles
            left = {currDeck.begin(), currDeck.begin() + n/2};
            right = {currDeck.begin() + n/2, currDeck.end()};
        } else { // Odd number of cards
            if (word == "out") { // First half has 1 more card than second half for out shuffles
                left = {currDeck.begin(), currDeck.begin() + n/2 + 1};
                right = {currDeck.begin() + n/2 + 1, currDeck.end()};
            } else { // Second half has 1 more card than first half for in shuffles
                left = {currDeck.begin(), currDeck.begin() + n/2};
                right = {currDeck.begin() + n/2, currDeck.end()};
            }
        }

        if (word == "out") {
            vector<int> v = left;
            for (int i=0; i<n; i++) {
                currDeck[i] = v[i/2]; // i/2 so that it only increments by 1 after 2 loops

                // Below if statement alternates making v = right or left card piles
                // So that start with left and alternate left -> right -> left -> ...
                if (i % 2 == 0) {
                    v = right;
                } else {
                    v = left;
                }
            }
        } else {
            vector<int> v = right;
            for (int i=0; i<n; i++) {
                currDeck[i] = v[i/2];

                // Same as above, but start with right and alternate right -> left -> right -> ...
                if (i % 2 == 0) {
                    v = left;
                } else {
                    v = right;
                }
            }
        }
    }
    while (currDeck != oldDeck); // Do this shuffling while currDeck is not oldDeck. Current deck is not the same arrangement as initial deck

    // Output number of shuffles needed
    cout << shuffles << endl;
}