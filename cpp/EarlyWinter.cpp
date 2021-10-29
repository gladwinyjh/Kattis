#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n, dm;

    cin >> n >> dm;

    vector<int> v(n);

    for (auto& i : v) {
        cin >> i;
    }

    for (int i=0; i<v.size(); i++) {
        if (v[i] <= dm) {
            cout << "It hadn't snowed this early in " << i << " years!" << endl;
            return 0;
        }
    }

    cout << "It had never snowed this early!" << endl;
}