#include <iostream>
#include <vector>

using namespace std;

int main(){
    // Duration vector to store number of trucks parked
    vector<int> parking(100, 0);
    int A, B, C;
    string start, end;

    cin >> A >> B >> C;

    for (int i=1; i<4; i++) {
        cin >> start >> end;

        // For the given duration, an additional truck was parked
        for (int j=stoi(start); j<stoi(end); j++) {
            parking[j] ++;
        }
    }

    int sum = 0;
    // Sum up how much Luka needs to pay by getting duration with fee per minute for EACH truck
    for (const auto& val : parking) {
        if (val == 1) {
            sum += A;
        } else if (val == 2) {
            sum += 2 * B;
        } else if (val == 3) {
            sum += 3 * C;
        }
    }
    cout << sum << endl;
}