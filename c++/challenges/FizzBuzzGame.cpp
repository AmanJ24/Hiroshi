#include <iostream>


using namespace std;



int main(){

    for(int i = 1; i <= 100; i++)
    {
        if(i % 3 == 0 && i % 5 == 0)
        {
            cout <<"Fizz Buzz" << endl;
            continue;
        }
        else if(i % 3 == 0)
        {
            cout <<"Fizz" << endl;
            continue;
        }
        else if(i % 5 == 0)
        {
            cout <<"Buzz" << endl;
            continue;
        }
        else{
            cout << i << endl;
        }

    }
    return 0;
}