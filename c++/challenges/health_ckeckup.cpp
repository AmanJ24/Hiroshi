#include <iostream>
using namespace std;

int main() 
{ 
    char wanna_continue_again;
    do{ 
    cout << "Enter your height in m: ";
    float height = 0;
    cin>>height;

    cout << "Enter your weight in kg: ";
    float weight = 0;
    cin>>weight;

    cout << "Your height is: " << height << " and your weight is " << weight << endl;
    cout << " Are you sure you entered right: " << endl;

    float BMI = weight / (height * height);
    char yes_or_not;
    cin>>yes_or_not;
    if(yes_or_not == 'y' || yes_or_not == 'Y')
    {
        if(BMI < 18.5f)
        {
            cout << "Your are underweight" << endl;
        }
        else if(BMI >= 18.5f && BMI <= 25.0f)
        {
            cout << "Your have a normal weight" << endl;
        }
        else if(BMI >= 25.0f && BMI < 30.0f)
        {
            cout << "You are slightly overweight " << endl;
        }
        else if(BMI >= 30.0f && BMI <= 35.0f)
        {
            cout << "You are obese "<< endl;
        }
        else if(BMI > 35.0f)
        {
            cout << "You are clinically obese" << endl;
        }
        
    }
    else{
        cout << "Fuck off" << endl;
    }
     cout << "If you wanna continue then press y or Y" << endl;
     cin>>wanna_continue_again;
        }
        while(wanna_continue_again == 'y'|| wanna_continue_again == 'Y'); 
}