#include <iostream>
using namespace std;

// Function to add two integers
int add(int a, int b) {
    return a + b;
}

// Function to add three integers
int add(int a, int b, int c) {
    return a + b + c;
}

// Function to add two double values
double add(double a, double b) {
    return a + b;
}

int main() {
    int sum1, sum2;
    double sum3;

    // Calling overloaded functions
    sum1 = add(10, 20);             // Calls add(int, int)
    sum2 = add(10, 20, 30);         // Calls add(int, int, int)
    sum3 = add(10.5, 20.5);         // Calls add(double, double)

    cout << "Sum1: " << sum1 << endl;
    cout << "Sum2: " << sum2 << endl;
    cout << "Sum3: " << sum3 << endl;

    return 0;
}
