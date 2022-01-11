#include <iostream>
#include <vector>
#include <stdlib.h>


using namespace std;


//declaring user input variables which i am using them in user_input;
char user_choice; 
bool x_or_o = true; 
char single_or_multiplayer;
bool nothing = false;



//player name variable here;
string first_player_name;
string second_player_name;



// string players_name();
bool if_tie(vector<vector<char>> &);
bool if_X(vector<vector<char>> &);
bool if_O(vector<vector<char>> &);
void multiplayer(vector<vector<char>> &);
void single_player(vector<vector<char>> &);
void tic_tac_toe_box(vector <vector<char>> &);



int main(){

vector <vector<char>>x_o{

    {'1',     '2',      '3'},
    {'4',     '5',      '6'},
    {'7',     '8',      '9'},
};

    system("CLS");
    cout << "Do you want to play Multiplayer or with bot: " << endl;
    cout << "Press S to play Alone || Press M to player multiplayer:  ";
    cin>>single_or_multiplayer;


    cout << "Press numeric keys to play this game: " << endl;


    system("CLS");

    tic_tac_toe_box(x_o);
    if(single_or_multiplayer == 'M' || single_or_multiplayer == 'm')
    {
        // players_name();
        multiplayer(x_o);
    }
    else if(single_or_multiplayer == 'S' || single_or_multiplayer == 's')
    {
        single_player(x_o);
    }


    return 0;
}


void tic_tac_toe_box(vector <vector<char>> &vector_ptr){

    cout << "|               |                |               |" << endl;
    cout << "|        "<<vector_ptr[0][0]<<"      |       "<< vector_ptr[0][1]<<"        |       "<<vector_ptr[0][2]<<"       |" << endl;
    cout << "|_______________|________________|_______________|" << endl; 
    cout << "|               |                |               |" << endl;
    cout << "|        "<<vector_ptr[1][0]<<"      |       "<<vector_ptr[1][1]<<"        |       "<<vector_ptr[1][2]<<"       |" << endl;
    cout << "|_______________|________________|_______________|" << endl;
    cout << "|               |                |               |" << endl;
    cout << "|        "<<vector_ptr[2][0]<<"      |       "<<vector_ptr[2][1]<<"        |       "<<vector_ptr[2][2]<<"       |" << endl;
    cout << "|               |                |               |" << endl;
}




void single_player(vector<vector<char>> &vector_ptr) {

    cout << "I am Working on it now:" << endl;
    cout << "Sorry" << endl;
}




void multiplayer(vector<vector<char>> &vector_ptr) {

    do{
        if(x_or_o == true)
        {
            if_X(vector_ptr);
            tic_tac_toe_box(vector_ptr);
            for (int i = 0; i < 3; i++)
            {
            
            
                if(vector_ptr[i][0] == vector_ptr[i][1] && vector_ptr[i][0] == vector_ptr[i][2] || vector_ptr[0][i] == vector_ptr[1][i] && vector_ptr[0][i] == vector_ptr[2][i])
                {
                    cout << "you won X" << endl;
                    nothing = true; 
                }
                
            } 
            if(vector_ptr[0][0] == vector_ptr[1][1] && vector_ptr[0][0] == vector_ptr[2][2] || vector_ptr[0][2] == vector_ptr[1][1] && vector_ptr[0][2] == vector_ptr[2][0])
            {
                cout << "You won X-";
                nothing = true;
            }
            if_tie(vector_ptr);

        }



        else if(x_or_o == false)
        {
            if_O(vector_ptr);
            tic_tac_toe_box(vector_ptr);
            for (int i = 0; i < 3; i++)
            {
            
            
                if(vector_ptr[i][0] == vector_ptr[i][1] && vector_ptr[i][0] == vector_ptr[i][2] || vector_ptr[0][i] == vector_ptr[1][i] && vector_ptr[0][i] == vector_ptr[2][i])
                {
                    cout << "you won O" << endl;
                    nothing = true; 
                }
                
            } 
            if(vector_ptr[0][0] == vector_ptr[1][1] && vector_ptr[0][0] == vector_ptr[2][2] || vector_ptr[0][2] == vector_ptr[1][1] && vector_ptr[0][2] == vector_ptr[2][0])
            {
                cout << "You won O";
                nothing = true;
            } 

            if_tie(vector_ptr);

        }

       
    }while(nothing != true);
 
   
}



bool if_X(vector<vector<char>> &vector_ptr){
            
    cout << "It's X turn: ";
    cin>>user_choice;

    if(user_choice == '1')
    {
        vector_ptr[0][0] = 'X';
    }


    else if(user_choice == '2')
    {
       vector_ptr[0][1] = 'X';
    }


    else if(user_choice == '3')
    {
        vector_ptr[0][2] = 'X';
    }


    else if(user_choice == '4')
    {
        vector_ptr[1][0] = 'X';
    }


    else if(user_choice == '5')
    {
        vector_ptr[1][1] = 'X';
    }


    else if(user_choice == '6')
    {
        vector_ptr[1][2] = 'X';
    }


    else if(user_choice == '7')
    {
        vector_ptr[2][0] = 'X';
    }


    else if(user_choice == '8')
    {
        vector_ptr[2][1] = 'X';
    }


    else if(user_choice == '9')
    {
        vector_ptr[2][2] = 'X';
                
    }
            
    system("CLS");
    x_or_o = false;
    return x_or_o;
        
}



bool if_O(vector<vector<char>> &vector_ptr){


    cout << "It's O turn: ";
    cin>>user_choice;
    if(user_choice == '1')
    {
        vector_ptr[0][0] = 'O';
    }


    else if(user_choice == '2')
    {
        vector_ptr[0][1] = 'O';
    }


    else if(user_choice == '3')
    {
        vector_ptr[0][2] = 'O';
    }


    else if(user_choice == '4')
    {
        vector_ptr[1][0] = 'O';
    }


    else if(user_choice == '5')
    {
        vector_ptr[1][1] = 'O';
    }


    else if(user_choice == '6')
    {
        vector_ptr[1][2] = 'O';
    }


    else if(user_choice == '7')
    {
        vector_ptr[2][0] = 'O';
    }


    else if(user_choice == '8')
    {
        vector_ptr[2][1] = 'O';
    }


    else if(user_choice == '9')
    {
        vector_ptr[2][2] = 'O';
                
    }
    system("CLS");    
    x_or_o = true;
        
    return x_or_o;
}


//This is to check if the game is tie or not;

bool if_tie(vector<vector<char>> &vector_ptr){

    int c = 0;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if(vector_ptr[i][j] == 'O' || vector_ptr[i][j] == 'X')
            { 
                c++;
                if(c == 9)
                {
                    cout << "Game tie";
                    nothing = true;
                }
            }
        }
        
    }
    
    return nothing;
}

