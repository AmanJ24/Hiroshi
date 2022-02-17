#ifdef _WIN32_
#include<iostream>
#include <stdlib.h>
#include <time.h>
#endif

// #ifdef linux
#include <iostream>
#include <stdlib.h>
#include <time.h>
// #endif
using namespace std;

void clear_screen();
int main(){
    clear_screen();
    bool win = false;
    cout << "======================================"<< endl;
    cout << "  ___    __    ___  ____  _  _  _____ " << endl;
    cout << " / __)  /__\  / __)(_  _)( \( )(  _  )" << endl;
    cout << "( (__  /(__)\ \__ \ _)(_  )  (  )(_)( " << endl;
    cout << " \___)(__)(__)(___/(____)(_)\_)(_____)" << endl;
    cout << "======================================" << endl;

    cout << "Enter Player Name: ";
    string player_name;
    getline(cin,player_name);

    cout << "Desposit Your Amount: ₹";
    int amount = 0;
    cin >> amount;

    do{
        cout << "Amount: " << amount << endl;
        cout << "How much money you want to bet ";

        int player_money = 0;
        cin>>player_money;



        amount -= player_money;
        cout << "Guess your number between (1 to 10): ";


        int guess_number = 0;
        cin>>guess_number;
        int random_number = 0;
        srand(time(NULL));

        random_number = (rand() % 10) + 1;   

        if(guess_number == random_number){
            player_money *= 10;
            amount = player_money;
            cout << "You are right" << endl;
        }
        else{
            cout << "FUCK OFF" << endl;
        }
        if(amount == 0){
            cout << "good news you lost all you money" << endl;
        }
    }while(amount != 0);
}




void clear_screen(){
    #ifdef _WIN32
    system("CLS");
    #else
    system("clear");
    #endif
}