#include <iostream>
using namespace std;

class Car {
public:
    string color, model;

    void displayInfo() {
        cout << "Model: " << model << ", Color: " << color << endl;
    }
};

int main() {
    Car myCar;

    myCar.color = "Red";
    myCar.model = "Toyota";

    myCar.displayInfo();

    return 0;
}


