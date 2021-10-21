#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int x, y;
    
    cin >> x >> y;
    if (x==0 && y==1) {
        cout << "ALL GOOD" << endl;
    } else if (y==1) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << setprecision(7) << x/(1.0-y)<< endl;
    }
}