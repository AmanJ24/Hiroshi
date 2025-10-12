#include <iostream>
using namespace std;

// Base class 1
class Animal {
public:
    void speak() {
        cout << "Animal sound" << endl;
    }
};

// Base class 2
class Vehicle {
public:
    void honk() {
        cout << "Beep" << endl;
    }
};

// Derived class (Multiple inheritance)
class RoboDog : public Animal, public Vehicle {
public:
    void speak() {
        cout << "Robo Bark" << endl;
    }
};

int main() {
    RoboDog robodog;
    robodog.speak();  // Output: Robo Bark
    robodog.honk();   // Output: Beep
    return 0;
}

