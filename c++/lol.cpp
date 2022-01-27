#include <iostream>

using namespace std;

int main(){

    long something = 7297804345;
    short length = 0;
    for (size_t i = 0; something > 0; length++)
    {
        cout << something << endl;
        something = something / 10;
    }
    cout << length << endl;
}