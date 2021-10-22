#include <unordered_map>
#include <iostream>

using namespace std;

int main(){
    unordered_map<string, int> counter;
    string name;

    // Store inputs in map
    while (getline(cin, name)) {
        if (name == "***") {
            break;
        }
        counter[name] ++;
    }

    int max_count = 0;
    string max_name;

    // Extract the name and its associated max frequency
    for (const auto& entry : counter) {
        if (entry.second > max_count) {
            max_count = entry.second;
            max_name = entry.first;
        }
    }

    // Check for multiple names with same max frequency
    for (const auto& entry : counter) {
        if (entry.second == max_count && entry.first != max_name) {
            cout << "Runoff!" << endl;
            return 0;
        }
    }
    cout << max_name << endl;
}