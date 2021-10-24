#include <iostream>
#include <algorithm>  
#include <vector> 

using namespace std;

#define pb push_back


int main(){
    int n1, n2, n3;
    vector <int> numbers;
    cin >> n1 >> n2 >> n3;
    numbers.pb(n1);
    numbers.pb(n2);
    numbers.pb(n3);

    sort(numbers.begin(), numbers.end());
    // The smaller difference is always the right difference
    if (numbers[1] - numbers[0] == numbers[2] - numbers[1]) {
        // Difference between 2nd and 1st number is same as that for 3rd and 2nd number
        // All 3 numbers are equally spaced, then the 4th number must be after the 3rd number
        cout << numbers[2] + (numbers[2] - numbers[1]) << endl;
    } else if (numbers[1] - numbers[0] > numbers[2] - numbers[1]) {
        // Difference between 2nd and 1st number is larger than that for 3rd and 2nd number
        // Add the smaller difference to the 1st number
        cout << numbers[0] + (numbers[2] - numbers[1]) << endl;
    } else {
        // Difference between 2nd and 1st number is smaller than that for 3rd and 2nd number
        // Add the smaller difference to the 2nd number
        cout << numbers[1] + (numbers[1] - numbers[0]) << endl;
    }
}