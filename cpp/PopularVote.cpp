#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator> 

using namespace std;

// Function to determine winner
void getWinner(vector<int>& counter) {
    // Number of total votes
    int numVotes = 0;
    // Maximum votes for a candidate
    int max = *max_element(counter.begin(), counter.end());
    // Index of the winner
    int winnerIndex = -1;

    for (int j=0; j<counter.size(); j++) {
        numVotes += counter[j];

        // Current candidate has max number of votes
        if (counter[j] == max) {
            // Winner has not yet been established
            if (winnerIndex == -1) {
                // Set current candidate as the winner. +1 because candidate no. start from 1.
                winnerIndex = j+1;
            } else {
                // There is more than 1 candidate with the max no. of votes
                cout << "no winner" << endl;
                return;
            }
        }
    }
    // Winner has more than half of total votes (majority), else minority
    if (max > numVotes / 2) {
        cout << "majority winner " << winnerIndex << endl;
    } else {
        cout << "minority winner " << winnerIndex << endl;
    }
}

int main(){
    int t, n, vote;
    
    cin >> t;
    for (int i=0; i<t; i++) {
        cin >> n;
        // To store votes for each candidate. Each start from 0.
        vector<int> counter(n, 0);

        // Store votes
        for (int j=0; j<n; j++) {
            cin >> vote;
            counter[j] += vote;
        }
        // Get winner
        getWinner(counter);
    }
}