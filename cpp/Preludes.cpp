#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main(){
    // To keep track of case #
    int i = 1;
    string input;

    while(getline(cin, input)) {
        string scale, tonality;
        stringstream ss(input);

        ss >> scale;
        ss >> tonality;

        // Scales that are of length 1 do not have alternative names
        if (scale.length() == 1) {
            cout << "Case " << i << ": " << "UNIQUE" << endl;
            i ++;
            continue;
        }

        // Replace scale with alternative scale name
        if (scale == "A#") {
            scale = "Bb";
        } else if (scale == "Bb") {
            scale = "A#";
        } else if (scale == "C#") {
            scale = "Db";
        } else if (scale == "Db") {
            scale = "C#";
        } else if (scale == "D#") {
            scale = "Eb";
        } else if (scale == "Eb") {
            scale = "D#";
        } else if (scale == "F#") {
            scale = "Gb";
        } else if (scale == "Gb") {
            scale = "F#";
        } else if (scale == "G#") {
            scale = "Ab";
        }  else if (scale == "Ab") {
            scale = "G#";
        } 

        cout << "Case " << i << ": " << scale << " " << tonality << endl;
        i ++;
    }
}