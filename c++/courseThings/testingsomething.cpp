#include <iostream>
#include <vector>
using namespace std;

class pro{
    public:
    int health;
    virtual void talk(){
        cout << "Pro is here" << endl;
    }
};

class noob: public pro{
    public:
    virtual void talk(){
        cout << "noob is here" << endl;
    }
};
int main(){
    pro* manveer = new noob;
    manveer->talk();

    return 0;
}