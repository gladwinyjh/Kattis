#include <iostream>
#include <limits> 
#include <vector>

using namespace std;

int getMaxWeight(vector<int>& elements, vector<int>& mIndex, int m) {
    int globalMax = numeric_limits<int>::min();

    for (int i=0; i<mIndex.size(); i++) {
        int back = 0;
        int front = 0;

        // Traverse backwards from current m till element is <=m
        // Sum up elements
        for (int j=mIndex[i]-1; j>=0; j--) {
            if (elements[j] <= m) {
                break;
            }
            back += elements[j];
        }

        // Traverse forwards from current m till element is <=m
        // Sum up elements
        for (int j=mIndex[i]+1; j<elements.size(); j++) {
            if (elements[j] <= m) {
                break;
            }
            front += elements[j];
        }

        // Local max = sum of forward + sum of backward + m
        int localMax = front + back + m;
        globalMax = max(localMax, globalMax);
    }

    return globalMax;
}

int main(){
    int t;

    cin >> t;

    for (int i=0; i<t; i++) {
        int n, m;
        // Store elements
        vector<int> elements;
        // Store positions of m
        vector<int> mIndex;

        cin >> n >> m;

        for (int i=0; i<n; i++) {
            int e;
            cin >> e;

            if (e == m) {
                mIndex.push_back(i);
            }

            elements.push_back(e);
        }

        cout << getMaxWeight(elements, mIndex, m) << endl;
    }
}