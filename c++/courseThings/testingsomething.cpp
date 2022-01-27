#include <iostream> 
using namespace std;


void something1(int &&lo);
void something1(int &lo);


int main(){

    int x = 100;
    something1(100);
    return 0;
}
void something1(int &&lo){ 
    cout << lo << endl;
}
void something1(int &lo){
    cout << lo << endl;
}