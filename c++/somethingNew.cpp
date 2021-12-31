#include <iostream>

using namespace std;


int nothing(int, int);
int main(){

    int hello;
    cout << "Hello World" << endl;
    // cout << hello << endl;

    cout << nothing(10,20) << endl;;
    return 0;
}


int nothing(int x , int y)
{
    int result = x + y;
    return result;
}