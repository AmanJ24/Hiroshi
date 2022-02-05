#include <iostream> 
using namespace std;

class pro{
    public:
    int infinite_health;
    int infinite_xp;


    pro(){

    }

    pro& operator=(const pro& other){
        this->infinite_xp = other.infinite_xp;
        this->infinite_health = other.infinite_health;
        return *this;
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
int main(){
    pro manveer;

    manveer.infinite_health = 100;
    manveer.infinite_xp = 230;

    cout << manveer;
    cin>>manveer;
    cout << manveer;
}