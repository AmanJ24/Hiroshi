#include <iostream>

using namespace std;
class pro{
    public:

    int something = 1;
    int xp = 1;

    pro(){

    }

    pro operator+(const pro& other){
        this->something = other.something;
        this->xp = other.xp;
        return *this;
    }
    void talk(){
        cout << "HELLO manveer" << endl;
    }
};

int main(){
    pro manveer;
    pro sakshi;

    manveer.something = 1024;

    sakshi = sakshi.operator+(manveer);
}
