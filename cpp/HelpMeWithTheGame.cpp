#include <iostream>
#include <istream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

// Vector to store white and black pieces
vector<string> white, black;
// Map to rank types of chess pieces
// So that comparator can get ordering from map values
unordered_map<char, int> mapOrder = 
    {   
        {'K', 1}, 
        {'Q', 2}, 
        {'R', 3}, 
        {'B', 4}, 
        {'N', 5},
        {'P', 6}
    };

// White Comparator
bool whiteCmp(string lhs, string rhs) {
    if (lhs.length() == rhs.length()) {
        if (lhs.length() == 2) {
            if (lhs[1] == rhs[1]) {
                return lhs[0] < rhs[0];
            } 
            return lhs[1] < rhs[1];
        } else {
            if (mapOrder[lhs[0]] == mapOrder[rhs[0]]) { // Same piece
                if (lhs[2] == rhs[2]) { // Same row
                    return lhs[1] < rhs[1]; // Smaller col first
                }
                return lhs[2] < rhs[2]; // Smaller row first
            } 
            return mapOrder[lhs[0]] < mapOrder[rhs[0]];
        }
    }
    return lhs.length() > rhs.length(); 
}

// Black Comparator
// Almost identical to white one. If there is a way to add a flag to check if white or black vector will be great...
bool blackCmp(string lhs, string rhs) {
    if (lhs.length() == rhs.length()) { // Same length
        if (lhs.length() == 2) { // Both pieces are pawns/same type
            if (lhs[1] == rhs[1]) { // Both pieces are on the same row
                return lhs[0] < rhs[0]; // Smaller column letter before larger one
            } 
            return lhs[1] > rhs[1]; // Larger row number before smaller one (THIS PART IS DIFFERENT FROM WHITE)
        } else { // Pieces are K, Q, R, B, or N
            if (mapOrder[lhs[0]] == mapOrder[rhs[0]]) { // Both pieces are same type
                if (lhs[2] == rhs[2]) { // Both pieces are on the same row
                    return lhs[1] < rhs[1]; // Smaller column letter before larger one
                }
                return lhs[2] > rhs[2]; // Larger row number before smaller one (THIS PART IS DIFFERENT FROM WHITE)
            } 
            // Both pieces are of different types.
            // Check map values for the pieces. Smaller integer before larger one
            return mapOrder[lhs[0]] < mapOrder[rhs[0]];
        }
    }
    // Left and right string are of different lengths. Longer length before shorter length
    return lhs.length() > rhs.length(); 
}

// Function to add a piece to white or black vectors
void addPiece(string piece, bool b) {
    if (b) { // if black piece
        black.push_back(piece);
    } else { // if white piece
        white.push_back(piece);
    }
}

int main() {
    // Current row of interest
    char row = '8';

    for (int i=0; i<17; i++) { // 17 total number of rows of input lines
        // Current col of interest
        char col = 'a';
        string input;
        getline(cin, input); // Read line of characters

        if (input[0] == '|') { // There are chess pieces in this line
            for (int j=2; j<33; j+=4) { // Start from 3rd char, increment 4 each time to capture pieces in col
                char chessPiece = input[j];
                bool b = true; // True if piece is black
                if (mapOrder.count(toupper(chessPiece)) != 0) { // Valid piece as it is found in map
                    if (isupper(chessPiece)) {
                        b = false; // White piece as first char is uppercase
                    }

                    if (toupper(chessPiece) == 'P') { // Piece is pawn
                        auto piece = string(1, col) + row; // Piece = col + row
                        addPiece(piece, b); // Add piece to white/black vector
                    } else { // Non-pawn
                        auto piece = string(1, toupper(chessPiece)) + col + row; // Piece = upper(alphabet) + col + row
                        addPiece(piece, b); // Add piece to white/black vector
                    }
                }
                // Go to next column
                col ++; 
            }
            // After each row, go to one row below
            row --;
        }
    }

    // Sort both white and black pieces
    sort(white.begin(), white.end(), whiteCmp);
    sort(black.begin(), black.end(), blackCmp);

    cout << "White: ";
    for (int i=0; i<white.size(); i++) {
        cout << white[i];
        // ',' if not at last element
        if (i != white.size()-1) {
            cout << ",";
        }
    }

    cout << endl << "Black: ";
    for (int i=0; i<black.size(); i++) {
        cout << black[i];
        // ',' if not at last element
        if (i != black.size()-1) {
            cout << ",";
        }
    }
}