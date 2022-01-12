#include <iostream>
#include <time.h>
#include <vector>

using namespace std;

int* array(int* why );
int main(){

    int why = 90;

    int* value = array(&why);
    cout << * value;

    return 0;
}

int* array(int* why){

    int* lol = why;
    *why = 90 +76;
    
    return why;
}