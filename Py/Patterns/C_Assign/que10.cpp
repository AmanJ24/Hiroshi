#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
    double num = 123.456;

    cout << setw(10) << setfill('-'); 
    cout.setf(ios::fixed);
    cout << setprecision(2) << num << endl; 
    cout.unsetf(ios::fixed);
    cout << setw(10) << setfill('*') << num << endl; 

    return 0;
}





