#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;

    while (T > 0) {
        long P, R, F;
        cin >> P >> R >> F;

        int yearsElapsed = 0;
        while (P <= F) {
            P *= R;
            yearsElapsed ++;
        }
        cout << yearsElapsed << endl;
        T --;
    }
}