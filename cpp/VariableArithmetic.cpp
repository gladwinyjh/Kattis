#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

int main(){
    string input;
    unordered_map<string, int> map;

    while(getline(cin, input)) {
        vector<string> v;
        string output;

        // Tokenize string
        // Split string by whitespace delimiter and store tokens in vector v
        string token = "";
        for (int i=0; i<input.length(); i++) {
            if (input[i] == ' ') {
                v.push_back(token);
                token = "";
            } else {
                token = token + input[i];
                // To store last token
                if (i == input.length() - 1) {
                    v.push_back(token);
                }
            }
        }

        // Important conditions to not get runtime error
        if (token == input) {
            // End script if 0 is given
            if (input == "0") {
                break;
            // If input only gives a number OR
            // if input is an undeclared variable
            // Return the number or the variable
            } else if (isdigit(token[0]) || map.count(token) == 0) {
                cout << token << endl;
            // Variable is declared
            // Return value stored from map
            } else {
                cout << map[token] << endl;
            }
            // Go to next statement
            continue;
        }
        
        // Sum of declared variables and numbers
        int sum = 0;
        // Flag if there are undeclared variables
        bool namePresent = false;

        if (v[1] == "=") {
            // Store declaration in map as int
            map[v[0]] = stoi(v[2]);
            continue;
        } else {
            // Only concerned with operands since all operators are "+", go stride=2
            for (int i=0; i<v.size(); i+=2) {
                // Is a variable
                if (!isdigit(v[i][0])) {
                    // Is an undeclared variable
                    if (map.count(v[i]) == 0) {
                        namePresent = true;
                        // There is already a variable in the output string
                        // Subsequent variables need to have ' + ' appended to it
                        if (output.length() > 0) {
                            output.append(" + ");
                        }
                        // String is empty, just append variable
                        output.append(v[i]);

                    } else {
                        // Is a declared variable
                        // Add its value to sum
                        sum += map[v[i]];
                    }
                // Is a number
                } else {
                    // Add number to sum
                    sum += stoi(v[i]);
                }
            }
        }

        if (sum > 0) {
            // There are undeclared variables in output string
            // Insert ' + ' then the sum to the front of the string
            // so that it is '<sum> + <rest of string>'
            if (namePresent) {
                output.insert(0, " + ");
            }
            output.insert(0, to_string(sum));
        // Sum == 0 and there are no undeclared variables
        } else if (!namePresent) {
            // Just output the sum == 0
            cout << 0 << endl;
            continue;
        }

        // Output is in form: '<sum> + <rest of string>'
        for (auto i : output) {
            cout << i;
        }
        cout << endl;
    }
}