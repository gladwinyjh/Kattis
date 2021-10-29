#include <iostream>
#include <algorithm> 
#include <vector>

using namespace std;

int main(){
    int N, L, P, maxDistance = 0;
    
    cin >> N >> L >> P;

    vector<int> cars(N, 0);

    for (int i=0; i<P; i++) {
        int x;
        cin >> x;

        if (x > N * L) {
            // Passenger is beyond length of train
            // Distance to travel = Distance to last car (x-N*L) + distance to last car door (L/2)
                // [         ||<--------]-----x
            // Increment last car volume 
            maxDistance = max(maxDistance, x - N*L + L/2);
            cars[N-1] ++;
        } else if (x % L == 0) {
            // Distance to travel = distance to car door from an end (L/2)
                // Distance to travel = [------->||        ] 
                //                      x
                //                  OR
                // Distance to travel = [        ||<-------] 
                //                                         x
            maxDistance = max(maxDistance, L/2);
            if (x == N * L) {
                // Passenger is at end of train
                // Increment last car volume 
                cars[N - 1] ++;
            } else {
                // Increment next car volume (its 0 indexed, so x/L gives next car)
                cars[x/L] ++;
            }
        } else if (x % L < L/2) {
            // Distance to travel = [   x----->||         ]
            int distance = L/2 - (x % L);
            maxDistance = max(maxDistance, distance);
            cars[x/L] ++;
        } else {
            // Distance to travel = [        | |<-----x ]
            //                  OR
            // Distance to travel = [        |x|        ]                    
            int distance = (x % L) - L/2;
            maxDistance = max(maxDistance, distance);
            cars[x/L] ++;
        }
    }

    cout << maxDistance << endl << *max_element(cars.begin(), cars.end()) << endl;
}