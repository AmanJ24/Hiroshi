#include <iostream>
using namespace std;

class pro{
    public:
    virtual void print(ostream& out) const = 0;
    friend void operator<<(ostream& out, pro& lol){
        lol.print(out);
    }
};

class noob : public pro{
    public:
    virtual void print(ostream& out) const override{
        out << "Hello World" << endl;
    }
};
int main(){
    noob manveer;
    cout << manveer;
    return 0;
}