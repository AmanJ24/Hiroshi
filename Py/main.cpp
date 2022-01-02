#include <iostream>
#include <vector>

using namespace std;




int main()
{ 
    vector <int> hotaro {};
    float total = 0.0f, average = 0.0f; //this is used in average if else statement;
    int elements;
    int numbers;

    char what_they_want_to_do;


    do
    {


    cout << "\n\nP - Print numbers" << endl;
    cout << "A - Add a number" << endl;
    cout << "M - Display mean of the numbers" << endl;
    cout << "S - Display The smalles number" << endl;
    cout << "L - display the largest number" << endl;
    cout << "Q - Quit" << endl;
    cout << "\nEnter what you want to do: ";
    cin>>what_they_want_to_do;




        if(what_they_want_to_do == 'P' || what_they_want_to_do == 'p' || what_they_want_to_do == 'A' || what_they_want_to_do == 'a' || what_they_want_to_do == 'M' || what_they_want_to_do == 'm' || what_they_want_to_do == 'S' || what_they_want_to_do == 's' || what_they_want_to_do == 'L' || what_they_want_to_do == 'l' || what_they_want_to_do == 'Q' || what_they_want_to_do == 'q')
        {

            
            //This if satement will print all the elements of list if it have or pring list is empty if it is empty
            if(what_they_want_to_do  == 'P' || what_they_want_to_do == 'p')
            {   
                if(hotaro.size() != 0)
                {
                    cout << "\n\n[ ";
                    for(int i = 0; i < hotaro.size(); i++)
                    {
                        cout << hotaro.at(i) << ",";
                    }
                    cout << "]" << endl;
                }
                else {
                    cout << "\n\nList is empty" << endl;
                }
            }





            //This is to add elements to the list if user predeed to add elements;
            else if(what_they_want_to_do == 'A' || what_they_want_to_do == 'a')
            {
                cout << "\nHow much elements you want to add: ";
                cin>>elements;

                for(int i = 0; i < elements; i++)
                {   
                    int number;
                    cout << "Enter your " << i + 1 << " number: ";
                    cin>>number;
                    hotaro.push_back(number);
                }
            }   





            //This is to calculate the mean or average of the elements in the list and display it...;
            else if(what_they_want_to_do == 'M' || what_they_want_to_do == 'm')
            {
                if(hotaro.size() != 0){

                    for (int i = 0; i < hotaro.size(); i++)
                    {
                        total += hotaro.at(i);
                    }

                    average = total / hotaro.size();
                    cout << "\n\nAverage is: " << average << endl;
                }
                else{
                    cout << "\n\nUnable to calculate the mean - no data" << endl;
                }
            }




            //This is to display Smallest value in list;
            else if(what_they_want_to_do == 'S' || what_they_want_to_do == 's')
            {
                if(hotaro.size() != 0)
                {
                    int small = hotaro[0];

                    for(int i = 0; i < elements; i++)
                    {
                        if(small > hotaro[i])
                        {
                            small = hotaro[i];
                        }   
                    }
                cout << "\n\nThis is the smallest value in the list: " << small << endl;
                }
                else{
                    cout << "\n\nPlease add some numbers first:  Press A to add" << endl;
                    cin.get();
                }   
     
            }





            //This is to display Largest value in list;
            else if(what_they_want_to_do == 'L' || what_they_want_to_do == 'l')
            {
                if(hotaro.size() != 0)
                {
                    int large = hotaro[0];
                    for(int i = 0; i < elements; i++)
                    {
                        if(hotaro[i] > large)
                        { 
                            large = hotaro[i];
                        }
                    }
                cout << "\n\nThis is the largest value: "<<large << endl;
                }
                else{
                    cout << "\n\nPlease add some numbers first:  Press A to add" << endl;
                    cin.get();
                }
        
            }





            //to quite;
            else if(what_they_want_to_do == 'q' || what_they_want_to_do == 'Q')
            {
            cout << "Good bye" << endl;
            }

        }
        else{
            cout << "Unknown Selection, please try again" << endl;
        }
    } while (what_they_want_to_do != 'Q' && what_they_want_to_do != 'q');
    


    return 0;
}
