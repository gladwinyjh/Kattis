#include <iostream>

using namespace std;

int main() {
    int pieces[6] = {1, 1, 2, 2, 2, 8};

    for (int i=0; i<6; i++) {
        int pieceNumber;
        cin >> pieceNumber;

        cout << pieces[i]-pieceNumber << " ";
    }
}