#include <iostream>
using namespace std;


class pro{
    public:
    virtual void talk(){
        cout << "Hello , I am Pro" << endl;
    }
    
};

class noob : virtual public pro{
    public:
    void yo(){
        cout << "Hello, I am noob" << endl;
    }
};


class intermidiate : virtual public pro{
    public:
    void hi(){
        cout << "Hello , I am intermidiate" << endl;
    }
};


class lol : public noob, public intermidiate{
    public:
    void talk(){
        noob::talk();
    }
};
int main(){
    return 0;
}

