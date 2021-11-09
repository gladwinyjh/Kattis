#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// To check if position is still on the chessboard
bool validPos (char first, int second) {
    if (second > 0 && second < 7) {
        // For rank 1 to 6 inclusive, possible file is a to k inclusive
        return !(first > 'k' || first < 'a');
    } else if (second == 7) {
        // For rank 7, possible file is b to j inclusive
        return !(first > 'j' || first < 'b');
    } else if (second == 8) {
        // For rank 8, possible file is c to i inclusive
        return !(first > 'i' || first < 'c');
    } else if (second == 9) {
        // For rank 9, possible file is d to h inclusive
        return !(first > 'h' || first < 'd'); 
    } else if (second == 10) {
        // For rank 10, possible file is e to g inclusive
        return !(first > 'g' || first < 'e');
    } else if (second == 11) {
        // For rank 11, possible file is only f
        return !(first != 'f');
    } else {
        // All other positions not on the board 
        return !(first > 'k' || first < 'a' || second > 11 || second < 1);
    }
}

// Function to get all valid positions
// From the current position, explore each position outwards (6 each time)
// Check if next position is a valid position with validPos
// Returns vector of valid positions 
vector<pair<char, int>> getPositions(pair<char, int>& pos) {
    // FOR BOTTOM RIGHT TO TOP LEFT
    int j = 1; // Counter for steps to travel to the left of 'f' 
    int rank_forward = pos.second; // To store rank when at 'f' 

    // FOR TOP LEFT TO BOTTOM RIGHT
    int k = 1; // Counter for steps to travel to the left of 'f'
    int rank_backwards = pos.second; // To store rank when at 'f' for backwards
    int rank_forwards = pos.second; // To store rank when at 'f' for forwards

    vector<pair<char,int>> positions;

    // Traverse diagonally bottom left to top right, and vice versa
    for (int i=1; i<11; i++) {
        pair<char, int> valid;

        // Dont need to add current position to vector
        if (i == 0) {
            continue;
        }

        // Traverse from starting position to bottom left
        if (pos.first - i < 'f') {
            // < 'f', file decreases as rank decreases
            if (validPos(pos.first - i, pos.second - j)) {
                valid = make_pair(pos.first-i, pos.second-j);
                positions.push_back(valid);
            }

            // Increment steps to travel
            // Important if traversing from >= 'f' to < 'f',
            // because 'i' cannot be used anymore
            j ++;

        } else if (pos.first - i >= 'f') {
            // >= 'f', file decreases as rank remains unchanged
            if (validPos(pos.first - i, pos.second)) {
                valid = make_pair(pos.first-i, pos.second);
                positions.push_back(valid);
            }
        }

        // Traverse from starting position to top right
        if (pos.first + i <= 'f') {
            // < 'f', file decreases as rank remains the same 
            if (validPos(pos.first + i, pos.second + i)) {
                valid = make_pair(pos.first+i, pos.second+i);
                positions.push_back(valid);
            }

            if (pos.first + i == 'f') {
                // Store rank when at 'f' for moving forward past 'f'
                rank_forward = pos.second + i;
            }

        } else if (pos.first + i > 'f') {
            // < 'f', file decreases as rank remains the same 
            if (validPos(pos.first + i, rank_forward)) {
                valid = make_pair(pos.first+i, rank_forward);
                positions.push_back(valid);
            }
        }
    }

    // Traverse diagonally top left to bottom right, and vice versa
    for (int i=1; i<11; i++) {
        pair<char, int> valid;

        // Dont need to add current position to vector
        if (i == 0) {
            continue;
        }

        // Traverse from starting position towards top left
        if (pos.first - i < 'f') {
            // < 'f', file decreases as rank remains the same 
            if (validPos(pos.first - i, rank_backwards)) {
                valid = make_pair(pos.first-i, rank_backwards);
                positions.push_back(valid);
            }

        } else if (pos.first - i >= 'f'){
            // >= 'f', file decreases as rank increases 
            if (validPos(pos.first - i, pos.second + k)) {
                valid = make_pair(pos.first-i, pos.second+k);
                positions.push_back(valid);
                
            }

            if (pos.first - i == 'f') {
                // Store rank when rook is at 'f'
                rank_backwards = pos.second + k;
            }

            // Rank decreases by 1 if file is >= 'f' towards top left
            // Important if traversing from < 'f' to >= 'f',
            // because 'i' cannot be used anymore
            k ++;
        }

        // Traverse from starting position towards bottom right
        if (pos.first + i <= 'f') {
            // <= 'f', file increases as rank remains the same
            if (validPos(pos.first + i, pos.second)) {
                valid = make_pair(pos.first+i, pos.second);
                positions.push_back(valid);
            }

            if (pos.first + i == 'f') {
                // Store rank when rook is at 'f'
                rank_forwards = pos.second;
            }

        } else if (pos.first + i > 'f'){
            // After 'f', file increases as rank decreases 
            if (validPos(pos.first + i, rank_forwards - 1)) {
                valid = make_pair(pos.first+i, rank_forwards-1);
                positions.push_back(valid);
                rank_forwards --; // Rank falls as move towards bottom right after 'f'
            }
        }
    }

    // Traverse up and down
    for (int i=-11; i<11; i++) {
        pair<char, int> valid;

        // Dont need to add current position to vector
        if (i == 0) {
            continue;
        }

        // Up and down. File remains the same while rank changes
        if (validPos(pos.first, pos.second + i)) {
            valid = make_pair(pos.first, pos.second+i);
            positions.push_back(valid);
        }
    }

    return positions;
}

int main() {
    string curr, aim;
    pair<char,int> start, end;
    vector<pair<char, int>> intermediate_positions;
    int numWays = 0;

    cin >> curr >> aim;

    // Process starting and ending positions
    // If rank given is 1 digit, process 2nd character. 
    // If 2 digits, process 2nd and 3rd character
    if (curr.length() == 2) {
        start = make_pair(curr[0], int(curr[1]) - '0');
    } else {
        start = make_pair(curr[0], stoi(curr.substr(1,2)));
    }

    if (aim.length() == 2) {
        end = make_pair(aim[0], int(aim[1]) - '0');
    } else {
        end = make_pair(aim[0], stoi(aim.substr(1,2)));
    }

    // Get all valid intermediate positions from starting positions
    intermediate_positions = getPositions(start);

    for (auto& pos : intermediate_positions) {
        if (pos == end) {
            // Need exactly 2 steps, so exclude 1 step ways
            continue;
        }

        // Get all valid final positions from each valid intermediate position
        vector<pair<char, int>> final_positions = getPositions(pos);

        for (auto& final_pos : final_positions) {
            if (final_pos == end) {
                // Increment if a next position from a current position == ending position
                numWays ++;
            }
        }
    }

    cout << numWays << endl;
}