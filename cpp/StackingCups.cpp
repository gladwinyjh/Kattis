#include <utility> 
#include <iostream>
#include <algorithm>  
#include <vector> 

using namespace std;

// Comparator to sort vector based on radius
bool cmp(pair<string, int> lhs, pair<string, int> rhs) {
    return lhs.second < rhs.second;
}

int main(){
    int n;
    string n1, n2;
    vector<pair<string, int> > cups;
    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> n1 >> n2;
        pair<string, int> cup;
        // If the radius is given first
        if (isdigit(n1[0]) == true) {
            // Half the radius
            int radius = stoi(n1)/2;
            // Store pair as (color, radius)
            cup = make_pair(n2, radius);
        } else {
            // Store pair as (color, radius)
            cup = make_pair(n1, stoi(n2));    
        }
        // Add pair to vector
        cups.push_back(cup);
    }

    // Sort vector based on radius
    sort(cups.begin(), cups.end(), cmp);

    for (int i=0; i<cups.size(); i++) {
        cout << cups[i].first << endl;
    }
}