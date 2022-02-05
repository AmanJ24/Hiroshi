#include <iostream> 
using namespace std;

class pro{
    public:
    int infinite_health;
    int infinite_xp;


    pro():infinite_health{0},infinite_xp{0}
    {

    }

    pro& operator=(const pro& other){
        this->infinite_xp = other.infinite_xp;
        this->infinite_health = other.infinite_health;
        return *this;
    }


    void add(int y, int lol){
        this->infinite_xp = y;
        this->infinite_health = lol;
    }
    friend void operator<<(ostream& out, pro& other)
    {
        out << other.infinite_xp << " " << other.infinite_health << endl;
    }
    
    friend void operator>>(istream&in , pro&other)
    {
        in >> other.infinite_xp;
    }

};

class noob : public pro{
    public:

    noob():pro(){

    }
    void add(int a , int b){
        cout << this->infinite_xp << " " << this->infinite_health<< endl;
        pro::add(a,b);
        cout << this->infinite_xp << " " << this->infinite_health<< endl;
    }
};
int main(){
    // pro manveer;

    // manveer.infinite_health = 100;
    // manveer.infinite_xp = 230;

    // cout << manveer;
    // cin>>manveer;
    // cout << manveer;

    noob someone;
    someone.add(100,200);
}