#include <iostream>
#include <cctype>
#include <cstring>
#include <string>


using namespace std;


int main(){

    // string hello = "hello world"; 
    // cout << hello << endl;

    string sentence = "nothings";
    string greetings = "hello world";

    string temp;

    temp = sentence + greetings;

    cout << temp;
    return 0;
}