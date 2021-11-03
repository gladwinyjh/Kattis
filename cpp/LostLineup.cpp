#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;


int main() {
    int n;
    string input;
    cin >> n;
    cin.ignore(); 
   
    vector<int> lineup(n-1);
    getline(cin, input); 
    stringstream ss(input);

    for (int i=0; i<n-1; i++) {
        int d;
        // Feed integers into lineup
        ss >> d;
        // i+2 represents the index of the current person in the queue
        lineup[d] = i+2;
    }

    cout << 1;
    for (int k=0; k<lineup.size(); k++) {
        cout << " " << lineup[k];
    }
}