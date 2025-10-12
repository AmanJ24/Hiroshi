#include <iostream>
using namespace std;

class Z{
    public:
    Z() { cout << "Constructor called." << endl;}

    ~Z() { cout << "Destructor called." << endl;}

};

int main(){
    Z z1;
    int a = 1;
    if (a == 1){
        Z z2;
    }
}