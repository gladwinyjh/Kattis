#include <iostream>
#include <algorithm>  
#include <vector>
#include <unordered_map> 

using namespace std;

int main(){
    int n;
    unordered_map<string, int> map;

    cin >> n;

    for (int i=0; i<n; i++) {
        vector<string> courses;
        for (int j=0; j<5; j++) {
            string course;
            cin >> course;
            courses.push_back(course);
        }

        // Sort so that different permutation will be the same
        sort(courses.begin(), courses.end());
        
        // Vector to string for unordered map key
        string courseString;
        for (const auto& course : courses) {
            courseString += course;
        }
        // Add one student for this combination
        map[courseString] ++;
    }

    // Find the max number of students taking a combination
    int maxNum = 0;
    for (const auto& entry : map) {
        maxNum = max(maxNum, entry.second);
    }

    // There could be multiple combination of courses that have the max students
    // For each max combination, add the number of students up
    int count = 0;
    for (const auto& entry : map) {
        if (entry.second == maxNum) {
            count += entry.second;
        }
    }

    cout << count << endl;
}