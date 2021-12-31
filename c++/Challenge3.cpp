#include <iostream>
#include <cmath>

using namespace std;


int main(){ 

    double number_of_cans = 0;
    double wall_height = 0;
    double wall_width = 0;
    double coverage_per_can = 0;


    cout << "============================================================" << endl;
    cout << "Enter Height of the wall: ";
    cin>>wall_height;
    cout << "Enter width of the wall: ";
    cin>>wall_width;
    // cout << "Enter the coverage of cans:";
    // cin>>coverage_per_can;
    cout << "============================================================" << endl;
    // coverage_per_can = coverage_per_can * 5;

    number_of_cans = (wall_height * wall_width) / 5;

    cout <<"This value is in points: " <<number_of_cans << endl;
    cout << "You will need "<<round(number_of_cans) << " cans of paint." << endl;
    return 0;
}