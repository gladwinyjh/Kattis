#include <iostream>

using namespace std;

int main(){
    int n;
    int count = 0;

    cin >> n;
    while (n > 0) {
        int temp;
        cin >> temp;

        if (temp < 0) {
            count ++;
        }
        n --;
    }

    cout << count << endl;
}