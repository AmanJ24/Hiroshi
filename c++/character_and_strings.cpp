#include <iostream>
#include <cctype>
#include <cstring>
#include <string>

using namespace std;

int main(){

    char my_name[] = {"Manveer"};

    cout << my_name << endl;

    my_name[7] = 'S';

    cout << my_name << endl;

    // char my_name[8];

    // strcpy(my_name,"Frank");

    // cout << my_name << endl;


    // char first_name[20] = {};
    // char last_name[20] = {};
    // char full_name[50] = {};
    // char temp[50] = {};

    // cout << "Please enter your first name: ";
    // cin>>first_name;

    // cout << "Please enter your last name: ";
    // cin>>last_name;
    // cout << "================================================================" << endl;

    // cout << "Hello, "<< first_name << " your first name has " << strlen(first_name) << " Characters"<< endl;
    // cout << "and your last name, " << last_name << " has " << strlen(last_name) << " Characters"<< endl;
    // cout << "================================================================" << endl;


    // strcpy(full_name, first_name);
    // strcat(full_name, " ");
    // strcat(full_name, last_name);

    // cout << "Enter your full name: ";
    // cin.getline(full_name, 14);
    // cin.get();
    // cout << full_name << endl;


    // strcpy(temp, full_name);

    // if(strcmp(temp,full_name) == 0)
    // {
    //     cout << "Hello World" << endl;
    // }
    // else{
    //     cout << "Invalid" << endl;
    // }



//  this will convert your line in upper letters


    // cout << "Enter your full name: ";
    // cin.getline(full_name, 20);
    // for(size_t i = 0; i < strlen(full_name); i++)
    // {
    //     if(isalpha(full_name[i]))
    //     {
    //         full_name[i] = toupper(full_name[i]);
    //     }
    // }
    // cout << full_name << endl;


    // string part1 = "C++";
    // string part2 = "is a powerfull";


    // string powerfull = part1 + " " + part2 + " Language";

    // cout << powerfull << endl;

    // string s1 = "Manveer Singh";

    // for(int h1 : s1)
    // {
    //     cout << h1 << endl;
    // }


    // cout << "\n" << s1.substr(8,5);


    // string s1 = "This is a test";

    // cout << s1.find("This") << endl;
    // cout << s1.find("is") << endl;
    // cout << s1.find("a") << endl;


    cout << "Enter your full name: ";
    string full_name;
    getline(cin,full_name);
    cout << "Welcome: " << full_name << endl;

    return 0;
}