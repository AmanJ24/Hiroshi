#include <iostream>
#include <vector>

using namespace std;

int main(){

    int student_numbers = 0;
    int student_height_input = 0;
    int total = 0;
    vector <int> student_height {};
    char want_to_continue;

    do
    {
        cout << "This will calculate average student height" << endl;
        cout << "Enter how many student you have: ";
        cin>>student_numbers;

        for (int i = 0; i < student_numbers; i++)
        {
            if(student_numbers != 0)
            {
                cout << "Enter " << i + 1 << " student height: ";
                cin>>student_height_input;

                student_height.push_back(student_height_input);

                total += student_height.at(i);
            }
            else{
            cout << "Enter something, you bitch" << endl;
            }
        
        }   
    
        int average = 0;

        average = total / student_height.size();

        cout << "This is the average student height: "<< average << endl;

        cout << "\nDO you want to continue again, if yes then press 'Y' if no then 'N'" << endl;
        cin>>want_to_continue;
    
    } while (want_to_continue != 'q' || want_to_continue != 'Q');
    
   
        return 0;
}
