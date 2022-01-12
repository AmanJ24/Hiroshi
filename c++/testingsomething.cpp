#include <iostream>
#include <time.h>
#include <vector>

using namespace std;

int why = 90;
int* array();
int main(){



    int* value = array();
    cout <<  value;

    return 0;
}

int* array(){

    int* lol = &why;
    why = 90 +76;
    
    return &why;
}