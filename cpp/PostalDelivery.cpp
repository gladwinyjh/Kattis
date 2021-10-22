#include <utility> 
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, k;

bool cmp(pair<int, int> lhs, pair<int, int> rhs) {
    if (lhs.first == rhs.first) {
        return lhs.second > rhs.second;
    }
    return lhs.first > rhs.first;
}

int travel(vector<pair<int, int>>& v) {
    // Total distance travelled
    int distance = 0;
    // Excess letters from previous trip
    int excess = 0;
    for (int i=0; i<v.size(); i++) {
        int lettersDelivered = min(excess, v[i].second);
        v[i].second -= lettersDelivered;
        excess -= lettersDelivered;
        // If remaining number of letters > 0
        if (v[i].second > 0) {
            // Lower bound of number of trips needed to deliver remaining letters
            int trips = v[i].second / k;
            // If need additional trip to complete location
            if (v[i].second % k > 0) {
                // Do that one extra trip
                trips ++;
                // v[i] location has all letters delivered, 
                // but there is still spare capacity to carry more letters
                // so v[i-1] can have the remaining letters to be delivered to it for this trip
                excess += k - v[i].second % k;
            }
            // Distance increment by the number of roundabout trips * distance of each one 
            distance += trips * 2 * v[i].first;
        }
    }
    return distance;
}

int main(){
    vector<pair<int, int> > v1, v2;
    
    cin >> n >> k;

    for (int i=0; i<n; i++) {
        int x, t;
        pair<int, int> p;

        cin >> x >> t;
        // Make pair of (absolute distance, num letters)
        p = make_pair(abs(x), t);
        if (x > 0) {
            // Store positive directions in v1
            v1.push_back(p);
        } else {
            // Store negative directions in v2
            v2.push_back(p);
        }
    }
    // Sort both vectors based on ascending distance
    // If same distance, then number of letters to deliver
    sort(v1.begin(), v1.end(), cmp);
    sort(v2.begin(), v2.end(), cmp);

    cout << travel(v1) + travel(v2) << endl;
}