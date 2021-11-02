#include <iostream>
#include <istream>
#include <string>

using namespace std;

int main() {
    string board[8][8] = 
    {
        {"...",":::","...",":::","...",":::","...",":::"},
        {":::","...",":::","...",":::","...",":::","..."},
        {"...",":::","...",":::","...",":::","...",":::"},
        {":::","...",":::","...",":::","...",":::","..."},
        {"...",":::","...",":::","...",":::","...",":::"},
        {":::","...",":::","...",":::","...",":::","..."},
        {"...",":::","...",":::","...",":::","...",":::"},
        {":::","...",":::","...",":::","...",":::","..."},
    };
    
    for (int i=0; i<2; i++) {
        string input;
        string types = "KQRBN";
        int skip = 1;
        getline(cin, input); // Read line

        for (int j=7; j<input.length(); j+=skip) { // Pieces only start from 7th index. Skip len indices after.
            char type; 
            int col, row;

            if (types.find(input[j]) != string::npos) { // K, Q, R, B or N
                type = input[j];
                // Change char alphabet to value
                // -97 so that 'A' is at value 0, 'B' = 1, ...
                col = int(input[j+1]) - 97;
                // Convert char input to number by - '0'.
                // 8 - result as board increases from top to bottom
                row = 8 - (input[j+2] - '0');
                // Since length of piece is 3 and length of ',' after is 1, skip 3+1 characters
                skip = 4;

            } else { // Pawn
                type = 'P';
                // Change char alphabet to value
                // -97 so that 'A' is at value 0, 'B' = 1, ...
                col = int(input[j]) - 97;
                // Convert char input to number by - '0'.
                // 8 - result as board increases from top to bottom
                row = 8 - (input[j+1] - '0');
                // Since length of piece is 2 and length of ',' after is 1, skip 2+1 characters
                skip = 3;
            }

            // Check if first char in line is 'W' or 'B' to dictate color of pieces
            if (input[0] == 'B') {
                // Piece is black. Change type to lowercase 
                type = tolower(type);
            } 

            // Put the piece on the board
            board[row][col][1] = type;
        }
    }

    // Print the board
    for (auto& i: board) {
        cout << "+---+---+---+---+---+---+---+---+" << endl;
        cout << "|";
        for (auto& j: i) {
            cout << j << "|";
        }
        cout << endl;
    }
    cout << "+---+---+---+---+---+---+---+---+"; // Last row
}