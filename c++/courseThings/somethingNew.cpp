#include <iostream>

using namespace std;
class pro{
    public:
    int something = 1;
    int xp = 1;

    friend bool operator==(pro& other, pro& other1){
        cout << "Something good is going to happen!" << endl;
        return true;
    }
    pro(){

    }

    bool operator+(const pro& other){
        this->something = other.something;
        this->xp = other.xp;
        return true;
    }
    // bool operator==(const pro& other){
        // if(this->something == other.something)return 1;
        // else{
            // return 0;
        // }
    // }
    void talk(){
        cout << "HELLO manveer" << endl;
    }
};

int main(){
    pro manveer;

    pro sakshi;

    manveer == sakshi;
}   
