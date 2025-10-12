#include <iostream>
using namespace std;

class Base {
public:
    virtual ~Base() { cout << "Base destructor" << endl; } // Virtual destructor
};

class Derived : public Base {
public:
    ~Derived() override { cout << "Derived destructor" << endl; }
};

int main() {
    Base* obj = new Derived(); // Base pointer to Derived object
    delete obj; // Calls Derived's destructor, then Base's destructor
    return 0;
}
