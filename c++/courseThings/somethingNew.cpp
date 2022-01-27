#include <iostream>
using namespace std;


class pro{
    public:

    int something = 1;
    int xp = 1;

    pro(){

    }

    void operator==(const pro& other){
        this->something += other.something;
        this->xp += other.xp;
    }
    void talk(){
        cout << "HELLO manveer" << endl;
    }
};
int main(){
    pro manveer;
    pro sakshi;

    cout << manveer.something << endl;
    cout << manveer.xp << endl;


    manveer.operator==(sakshi);


    cout << manveer.something << endl;
    cout << manveer.xp << endl;
}
