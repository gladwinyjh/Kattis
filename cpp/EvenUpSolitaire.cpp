#include <iostream>
#include <stack>

using namespace std;

int main(){
    int n;
    stack<int> cards;

    cin >> n;

    for (int i=0; i<n; i++) {
        int input;
        cin >> input;

        // If stack is empty or if top of stack + input is odd, add card to top of stack
        if (cards.size() == 0 || (cards.top() + input) % 2 != 0) {
            cards.push(input);
        } else {
            cards.pop();
        }
    }
    // Print remaining number of cards in stack
    cout << cards.size() << endl;
}