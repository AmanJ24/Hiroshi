#include <iostream>
#include <vector>



using namespace std;
//global variables here;
vector <long long> phone_numbers;
vector <string> name;

// functions declare here;
void if_1();
void if_2();
void if_3();



int main(){
    char what_they_want_to_do;
    do{
        cout << "1. Do you want to add new phone record"<< endl;
        cout << "2. Do you want to show existing phone records" << endl;
        cout << "3. Do you want to delet phone record"<< endl;
        cout << "4. If you want to quit then presss Q" << endl;
        cout << "Select number: ";
        cin>>what_they_want_to_do;
        if(what_they_want_to_do == '1'){
            if_1();
        }
        else if(what_they_want_to_do == '2'){
            if_2();
        }
        else if(what_they_want_to_do == '3'){
            if_3();
        }

    }while(what_they_want_to_do != '4');
}


void if_1(){
    cout << "Enter Name: ";
    string input_name;
    cin>>input_name;
    name.push_back(input_name);


    cout << "Enter phone number: ";
    long input_number;
    long temp;
    temp = input_number;
    short length = 0;


    cin>>input_number;
    temp = input_number;
    for (size_t i = 0; temp > 0;)
    {
        temp = temp /10;
        length++;
    }
    if(length == 10){
        phone_numbers.push_back(input_number);
        cout << "Phone  number is added" << endl;
    }
    else{
        cout << "Bro you are live in INDIA enter 10 digit number: " << endl;
    }
}

void if_2(){
    if(name.size() != 0){

        for (int i = 0; i < name.size(); i++)
        {
            cout<<endl;
            cout << "Name: "<<name[i]<< " Phone Number: " <<phone_numbers[i]<< endl;
            cout<<endl;
        }
    }
    else{
        cout << "you don't have any contact number added: " << endl;
    }
    
}

void if_3(){
    for (int i = 0; i < name.size(); i++)
    {
        cout << i+1 <<  " Name: "<<name[i]<< " Phone Number: " << phone_numbers[i]<< endl;
    }
    
    cout << "Which number you want do delete: ";
    short which_number;
    cin>>which_number;
    which_number--;
    name.erase(name.begin() + which_number);

    
    if(phone_numbers.size() != 0){
        phone_numbers.erase(phone_numbers.begin() +which_number);
    }
    
}