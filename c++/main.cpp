#include <iostream>
#include <istream>
using namespace std;

int main()
{
    char selection;
    char temp;
    do{
        cout << "\n\n----------------------------------------------------------------"<< endl;
        cout << "1. Do this" << endl;
        cout << "2. Do that" << endl;
        cout << "3. Do something else" << endl;
        cout << "Q. Quit\n" << endl;
        cout << "Enter your selection: ";
        cin>>selection;

        if(selection == '1')
        {
            cout << "You chose 1 - doing this" << endl;
        }
        else if(selection == '2')
        {
            cout << "You chose 2 - doing that" << endl;
        }
        else if(selection == '3')
        {
            cout << "You chose 2 - do something else" << endl;
        }
        else if(selection == 'q' || selection == 'Q')
        {
            cout << "Goodbye" << endl;
        }
        else {
            cout << "unknown option -- try again" << endl;
        }
    }while(selection != 'q' && selection != 'Q');
    return 0;

}