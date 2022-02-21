#include <iostream>
#include <time.h>

using namespace std;

void print_introduction(int);


bool player_game(int difficulty){
    print_introduction(difficulty);

    srand(time(NULL));
    int code_a = (rand() % difficulty) + difficulty; 
    int code_b = (rand() % difficulty) + difficulty;
    int code_c = (rand() % difficulty) + difficulty;

    //doing sum and product of random number here; 
    int sum = code_a + code_b + code_c;
    int product = code_a * code_b * code_c;

    //printing the random number product and sum;
    cout << "There are 3 numbers in the code" << endl;
    cout <<"The codes ADD-up to: " << sum<< endl;
    cout <<"The coedes Multiply to give: " << product << endl;

    //taking input guess here;
    int guess_a , guess_b , guess_c;
    cin>>guess_a>>guess_b>>guess_c;

    //showing user their input;
    cout << "You entered: " << guess_a << guess_b << guess_c << endl;

    int guess_sum = guess_a + guess_b + guess_c;
    int guess_product = guess_a * guess_b * guess_c;

    //checking if the guess is correct or not;
    if(guess_sum == sum && guess_product == product){
        cout << "\n*** Well done agent! You have extracted a file! Keep going! ***" <<endl;
        return true;
    }
    else{
        cout << "\n*** You entered the wrong code! Careful agent! Try again! **\n" << endl;
        return false;
    }
}


void print_introduction(int level_difficulty){
    cout << "\n\nYou are a secret agent breaking into a level "<< level_difficulty<<" secure server room..."<<endl;
    cout << "You need to enter the correct codes to continue...\n\n" << endl;
}

int main(){
    int level_difficulty = 1;
    int max_difficulty = 5;


    while(level_difficulty <= max_difficulty){
        bool level_complete = player_game(level_difficulty);
        // player_game(level_difficulty);
        cin.clear();
        cin.ignore();
        if(level_complete){
            level_difficulty++;
        }
    }
    
    cout << "\n*** Great work agent! You got all the files! Now get out of there! ***\n";
    return 0;
}