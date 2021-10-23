#include <iostream>
#include <vector> 

using namespace std;

int main(){
    int n;
    float numVaccinated = 0;
    float numUnvaccinated = 0;
    vector<float> vaccinated = {0, 0, 0};
    vector<float> unvaccinated = {0, 0, 0};

    cin >> n;
    for (int i=0; i<n; i++) {
        string participant;

        cin >> participant;
        
        // Check vaccination status of participant
        if (participant[0] == 'Y') {
            numVaccinated ++;
        } else {
            numUnvaccinated ++;
        }

        // Iterate through infection status for 3 strains
        // If infected by strain, increment vaccinated[i] or unvaccinated[i] (depending on vaccination status)
        for (int j=1; j<4; j++) {
            if (participant[j] == 'Y') {
                if (participant[0] == 'Y') {
                    vaccinated[j-1] ++;
                } else {
                    unvaccinated[j-1] ++;
                }
            }
        }
    }

    // Caluculate respective percentages
    // If infection rates for vaccinated >= that for unvaccinated, not effective
    // Else get the fraction difference * 100 for percentage difference
    for (int i=0; i<3; i++) {
        float vaccinatedPercentage = vaccinated[i]/numVaccinated;
        float unvaccinatedPercentage = unvaccinated[i]/numUnvaccinated;
        
        if (vaccinatedPercentage >= unvaccinatedPercentage) {
            cout << "Not Effective" << endl;
        } else {
            cout << (unvaccinatedPercentage - vaccinatedPercentage)*100 / unvaccinatedPercentage << endl;
        }
    }
}