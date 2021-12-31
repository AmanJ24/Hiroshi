#include <iostream>
using namespace std;
 
int main()
{
    const int small_pizza = 15;
    const int medium_pizza = 20;
    const int large_pizza = 25;

    const int pepperoni_for_small_pizza = 2;
    const int pepperoni_for_medium_pizza = 3;
    const int pepperoni_for_large_pizza = 1;


    cout << "Welcome to our pizza shop. \n We offer three size pizza Large , Medium and Small" << endl;
    cout << "If you want Large size pizza press 1 \nIf you want Medium size pizza then press 2 \nif you want Small size pizza then press 3" << endl;
    int user_pizza_number = 0;
    cin>>user_pizza_number;

    if(user_pizza_number == 3)
    {
        cout << "Do you want to add pepperoni for your Large pizza\n press Y to add pepperoni for your small size pizza\n if you don't want do add pepperoni then press N" << endl;
        char user_pepperoni;
        cin>>user_pepperoni;
        if(user_pepperoni == 'y' || user_pepperoni == 'Y')
        {
            int total =0;
            total = large_pizza * pepperoni_for_large_pizza;
            cout << "Your total is: " << total << " Rupees"<< endl;
        }
        else 
        {
            cout << "Your total is: " << large_pizza << " Rupees" << endl;
        }
    }
    else if(user_pizza_number == 2)
    {
        cout << "Do you want to add pepperoni for your Medium pizza\n press Y to add pepperoni for your small size pizza\n if you don't want do add pepperoni then press N" << endl;
        char user_pepperoni;
        cin>>user_pepperoni;
        if(user_pepperoni == 'y' || user_pepperoni == 'Y')
        {
            int total =0;
            total = medium_pizza * pepperoni_for_medium_pizza;
            cout << "Your total is: " << total << " Rupees"<< endl;
        }
        else 
        {
            cout << "Your total is: " << medium_pizza << "Rupees" << endl;
        }
    }
    else if(user_pizza_number == 1)
    {
        cout << "Do you want to add pepperoni for your small pizza\n press Y to add pepperoni for your small size pizza\n if you don't want do add pepperoni then press N" << endl;
        char user_pepperoni;
        cin>>user_pepperoni;
        if(user_pepperoni == 'y' || user_pepperoni == 'Y')
        {
            int total =0;
            total = small_pizza * small_pizza;
            cout << "Your total is: " << total << "Rupees"<< endl;
        }
        else 
        {
            cout << "Your total is: " << small_pizza << "Rupees" << endl;
        }
    }
  
}