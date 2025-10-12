#include <iostream>
using namespace std;

class Base {
public:
    virtual void display() { cout << "Base display" << endl; }
};

class Derived : public Base {
public:
    void display() override { cout << "Derived display" << endl; }
};

int main() {
    Base* b;
    Derived d;
    b = &d;
    b->display();
    return 0;
}




