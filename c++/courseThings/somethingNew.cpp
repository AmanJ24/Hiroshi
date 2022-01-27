#include <iostream>
using namespace std;


class pro{
    public:

    int something = 1;
    int xp = 1;

    pro(){

    }

    pro operator+(const pro& other){
        this->something += other.something;
        this->xp += other.xp;
        return *this;
    }

    void operator-(void){
        this->something = 100;
        this->xp = 200;
        cout << this->xp << endl;
        cout << this->something << endl;
    }


    bool operator==(const pro& other){
        if(this->something == other.something)return true;
        else
            return false;
        
    }
    void talk(){
        cout << "HELLO manveer" << endl;
    }
};
int main(){
    pro manveer;
    pro sakshi;

    manveer.something = 100;
    sakshi.something = 100;
    sakshi = sakshi + manveer;
}
