#include <iostream>
#include <algorithm> 
#include <stack>
#include <unordered_map>

using namespace std;

int main(){
    int n;
    // Position of event in stack starting from 1
    int index = 1;
    // Map to keep track of position of events in stack. Key = event, val = index.
    unordered_map<string, int> map;
    // Stack to keep track of which events were last added
    stack<string> s;

    cin >> n;

    for (int i=0; i<n; i++) {
        string line;
        cin >> line;

        if (line == "E") {
            string event;
            cin >> event;

            // Add event to stack
            s.push(event);
            // Store event in map
            map[event] = index;
            // Increment index for next event
            index ++;
            
        } else if (line == "D") {
            int r;
            cin >> r;

            for (int j=0; j<r; j++) {
                // Remove key corresponding to last event
                map.erase(s.top());
                // Remove event from stack
                s.pop(); 
                // Decrement index for next event since one event has been removed
                index --;
            }
        } else if (line == "S") {
            int k;
            // To store position of the '!' event that is the closest to the back of the stack
            int dream = index;
            // To store position of other events that allegely occurred, and actually occurred
            int keep = -1;
            // Boolean to keep track if an event allegedly occurred but it never happened
            bool neverOccurred = false;
            cin >> k;

            for (int j=0; j<k; j++) {
                string e;
                cin >> e;

                if (e[0] == '!') {
                    // Event found in map, but scenario said it did not happen.
                    if (map.find(e.substr(1)) != map.end()) {
                        dream = min(dream, map[e.substr(1)]);
                    } // If event not found, then it does not matter
                } else {
                    if (map.find(e) != map.end()) {
                        keep = max(keep, map[e]);
                    } else {
                        // Scenario needs event, but event never occurred
                        neverOccurred = true;
                    }
                }
            }

            // We want to make sure that dream > keep because if dreamed indices are smaller 
            // than keep indices, then keep events have to be removed for dream events to be removed
            // thus making keep events from happening.
            // Ex: {D, K, K}
                // We cannot remove D because dream needs to remove the last 3 events, which
                // Means that the top 2 Ks will also be removed.
                // Then we cannot alleged that the Ks occurred anymore...

            if (dream == index && !neverOccurred) {
                cout << "Yes" << endl;
            } else if (keep >= dream || neverOccurred) {
                cout << "Plot Error" << endl;
            } else {
                cout << index - dream << " Just A Dream" << endl;   
            }
        }
    }
}