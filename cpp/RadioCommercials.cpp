#include <iostream>
#include <limits>
#include <vector>

using namespace std;

vector<int> net;

int Kadane() {
    int localBiggest = 0;
    int globalBiggest = numeric_limits<int>::min();

    for (int i=0; i<net.size(); i++) {
        localBiggest = max(net[i], net[i] + localBiggest);
        if (localBiggest > globalBiggest) {
            globalBiggest = localBiggest;
        }
    }
    return globalBiggest;
}

int main(){
    int N, P;

    cin >> N >> P;

    for (int i=0; i<N; i++) {
        int income;
        cin >> income;
        // Store net = income from students - price of commercial
        net.push_back(income-P);
    }
    
    cout << Kadane() << endl;
}