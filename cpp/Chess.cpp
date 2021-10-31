#include <iostream>
#include <utility>
#include <vector>

using namespace std;

// To check if position is still on the chessboard
bool validPos (char first, int second) {
    return !(first > 'H' || first < 'A' || second > 8 || second < 1);
}

// Function to get all valid positions from current position pos
// Returns vector of valid positions 
vector<pair<char, int>> getPositions(pair<char, int>& pos) {
    vector<pair<char,int>> positions;

    for (int i=-8; i<=8; i+=1) {
        // Dont need to add current position to vector
        if (i == 0) {
            continue;
        }

        // Add all valid diagonals to vector
        pair<char, int> valid;
        if (validPos(pos.first + i, pos.second + i)) {
            valid = make_pair(pos.first+i, pos.second+i);
            positions.push_back(valid);
        }

        if (validPos(pos.first + i, pos.second - i)) {
            valid = make_pair(pos.first+i, pos.second-i);
            positions.push_back(valid);
        }
    }

    return positions;
}

// Check if this position is directly diagonal to end position
// if absolute difference in between x_start and x_end is equal to y_start and y_end.
bool checkDiagonal (pair<char, int>& pos1, pair<char, int>& pos2) {
    return (abs(pos1.first - pos2.first) == abs(pos1.second - pos2.second));
}

int main(){
    int t;
    cin >> t;

    for (int i=0; i<t; i++) {
        int y1, y2;
        char x1, x2;
        pair<char, int> start, end;

        cin >> x1 >> y1 >> x2 >> y2;

        start = make_pair(x1, y1);
        end = make_pair(x2, y2);

        // Start and end positions are the same; 0 moves needed
        if (start.first == end.first && start.second == end.second) {
            cout << "0 " << start.first << " " << start.second << endl;
            continue;
        }

        // Start position is directly diagonal to end position; 1 move needed (move from start to end)
        if (checkDiagonal(start, end)) {
            cout << "1 " << start.first << " " << start.second << " ";
            cout << end.first << " " << end.second << endl;
            continue;
        }

        // Store copy of initial starting position
        pair<char, int> initialStart = start;
        // Vector to store all possible positions
        vector<pair<char, int>> positions;
        // Flag for if intermediate position from start to end is found
        bool found = false;

        // Get all possible positions from starting position
        positions = getPositions(start);

        // Go through all possible intermediate positions
        // Since the minimum number of moves needed is 2,
        // If it is possible to go from start to end, the intermediate position will be located.
        for (auto pos : positions) {
            // Check if this position is directly diagonal to end position
            if (checkDiagonal(pos, end)) {
                found = true;
                cout << "2 " << initialStart.first << " " << initialStart.second << " ";
                cout << pos.first << " " << pos.second << " ";
                cout << end.first << " " << end.second << endl;
                break;
            }
        }

        // Impossible to go from start to end
        if (!found) {
           cout << "Impossible" << endl;     
        }
    }
}