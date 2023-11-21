#include <iostream>
#include <vector>
#include <cctype>

using namespace std;


//Declaring Global variables;
char what_they_want_to_do;
int elements;





//declaring Functions;
char main_menu();
void print_value(vector<int>);
void add_value(vector<int> &);
void average(vector<int> &);
void smallest_number(vector<int> &);
void largest_number(vector<int> &);





int main(){
    vector <int> hotaro(9,0);
    

    do{
        
        main_menu();
        if(what_they_want_to_do == 'P' || what_they_want_to_do == 'p' || what_they_want_to_do == 'A' || what_they_want_to_do == 'a' || what_they_want_to_do == 'M' || what_they_want_to_do == 'm' || what_they_want_to_do == 'S' || what_they_want_to_do == 's' || what_they_want_to_do == 'L' || what_they_want_to_do == 'l' || what_they_want_to_do == 'Q' || what_they_want_to_do == 'q')
        {
            print_value(hotaro);
            add_value(hotaro);
            average(hotaro);
            smallest_number(hotaro);
            largest_number(hotaro);
            //cout << hotaro.at(0) << endl;
        }
        else{
            cout << "Unknown Selection, please try again" << endl;
        }  
    }while(what_they_want_to_do != 'q' && what_they_want_to_do != 'Q');
    
    return 0;
}



char main_menu(){

    cout << "\n\nP - Print numbers" << endl;
    cout << "A - Add a number" << endl;
    cout << "M - Display mean of the numbers" << endl;
    cout << "S - Display The smalles number" << endl;
    cout << "L - display the largest number" << endl;
    cout << "Q - Quit" << endl;
    cout << "\nEnter what you want to do: ";
    cin>>what_they_want_to_do;

    return toupper(what_they_want_to_do);
}




void print_value(vector <int> value){

    if(what_they_want_to_do == 'P' || what_they_want_to_do == 'p')
    {
        if(value.size() != 0){
            cout << "\n\n[ ";
            for (int i = 0; i < value.size(); i++)
            {
                cout << value.at(i) << ",";
            }
            cout << "]" << endl;
            
        }
        else{
            cout << "\n\nList is empty" << endl;
        }
    }
}





void add_value(vector<int> &value){

    if(what_they_want_to_do == 'A' || what_they_want_to_do == 'a')
    {

        cout << "\nHow much elements you want to add: ";
        cin>>elements;
        cout << elements << endl;

        for(int i = 0; i < elements; i++)
        {   
            int number;
            cout << "Enter your " << i + 1 << " number: ";
            cin>>number;
            value.push_back(number);
            //cout << value.at(i) << endl;
        }
        for (int i = 0; i < value.size(); i++)
            {
                cout << value.at(i) << ",";
            }
            
    } 
    // return value;
}




void average(vector <int> &value){

    if(what_they_want_to_do == 'M' || what_they_want_to_do == 'm')
    {
        int average = 0;
        int total = 0;
        if(value.size() != 0){

            for (int i = 0; i < value.size(); i++)
            {
                total += value.at(i);
            }

            average = total / value.size();
            cout << "\n\nAverage is: " << average << endl;
        }
        else{
            cout << "\n\nUnable to calculate the mean - no data" << endl;
        }
    }

}






void smallest_number(vector <int> &value){
    //This is to display Smallest value in list;
    if(what_they_want_to_do == 'S' || what_they_want_to_do == 's')
    {
        if(value.size() != 0)
        {
            int small = value[0];

            for(int i = 0; i < elements; i++)
            {
                if(small > value[i])
                {
                    small = value[i];
                }   
            }
            cout << "\n\nThis is the smallest value in the list: " << small << endl;
        }
        else{
            cout << "\n\nPlease add some numbers first:  Press A to add" << endl;
            // cin.get();
        }   
     
    }

}





void largest_number(vector <int> &value){

    //This is to display Largest value in list;
    if(what_they_want_to_do == 'L' || what_they_want_to_do == 'l')
    {
        if(value.size() != 0)
        {
            int large = value[0];
            for(int i = 0; i < elements; i++)
            {
                if(value[i] > large)
                { 
                    large = value[i];
                }
            }
            cout << "\n\nThis is the largest value: "<<large << endl;
        }
        else{
            cout << "\n\nPlease add some numbers first:  Press A to add" << endl;
            // cin.get();
        }
        
    }
}
