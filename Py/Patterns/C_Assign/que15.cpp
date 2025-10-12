#include <iostream>
using namespace std;

class Complex {
private:
    float real;
    float imag;

public:
    // Constructor
    Complex(float r, float i) : real(r), imag(i) {}

    // Overload + operator
    Complex operator + (const Complex& other) {
        return Complex(real + other.real, imag + other.imag);
    }

    // Function to display complex number
    void display() const {
        cout << real << " + " << imag << "i" << endl;
    }
};

int main() {
    Complex c1(2.5, 3.5);
    Complex c2(1.5, 2.5);
    Complex c3 = c1 + c2; // Uses overloaded + operator
    c3.display(); // Output: 4.0 + 6.0i
    return 0;
}
