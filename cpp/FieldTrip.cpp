#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int main(){
    int N;
    vector<int> buses(2, 0);
    vector<int> classSizes;

    cin >> N;

    for (int i=0; i<N; i++) {
        int section;
        cin >> section;
        classSizes.push_back(section);
    }

    // Get sum of total class sizes 
    int total = accumulate(classSizes.begin(), classSizes.end(), 0);

    // Bus capacity is flexible
    // Because we do not want teachers on buses
    // The sum of class sizes MUST be divisible by 3 so that all buses can be filled equally be students
    // If it is divisible, then the capacity for each bus is simply sum of class sizes / 3.
    if (total % 3 != 0) {
        cout << -1 << endl;
        return 0;
    }
    // To record index of bus currently being filled
    int j = 0;
    for (int i=1; i<=classSizes.size(); i++) {
        // Fill current bus with current class
        buses[j] += classSizes[i-1];

        // Filling current bus with current class size exceeds total/3.
        // Buses cannot be split evenly for the given class sizes (classes board bus sequentially)
        if (buses[j] > total/3) {
            cout << -1 << endl;
            break;
        
        // Current bus is full after recent class boards it
        // Print index of class and go to next bus
        } else if (buses[j] == total/3) {
            cout << i << " ";
            j ++;
        }

        // Only need output for first 2 buses. Break if bus index goes to 2 from 0.
        if (j == 2) {
            break;
        }
    }
}