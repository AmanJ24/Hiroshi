#include <iostream>
#include <string>



using namespace std;

int main(){
    string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string key = "vnjsjdfsjfwerowievrnowiebriewpqwierxmqpwoerwevrioewo";


    cout << "Enter your password with no space which i will encrypt: ";
    string password;
    getline(cin,password);



    string temp_password = password;
    for(int i=0; i < password.length(); i++)
    {
        for(int j=0; j < alphabet.length(); j++)
        {
            if(password[i] == alphabet[j])
            {
                // cout << key.at(j) << endl;
                password[i] = key[j];
                break;
            }

        }
    }
    


    cout << "This is your encrypted password: "<< password << endl;
    password = temp_password;
    cout << "And this is your dcrypt password: "<<password << endl;
    return 0;
}