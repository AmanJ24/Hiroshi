#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(){                                                                       
                                                                                          

    // int* first_pointer = 0;

    // string* your_name_pointer = nullptr;

    // cout << &your_name_pointer <<endl;


    // int* p = nullptr;

    // cout << p << endl;
    // cout << sizeof(p) << endl;

    // cout << "Enter your name: ";
    // char name[100];
    // cin.getline(name, 100);

    // cout << "Your name before reversing: "<<name<<endl;

    // for (int i = strlen(name) - 1; i>=0; i--)
    // {
    //     // name[i];
    //     cout << name[i];

    // }


    // int* p = nullptr; 
    // int a = 10;

    // p = &a;

    // cout << p << endl;
    // cout << &a << endl;
    // cout << sizeof(a) << endl;
    // cout << sizeof(p) << endl;
    // cout << &p << endl;


    // int num = 90;
    // int *p = nullptr;

    // p = &num;

    // cout << num << endl;
    // cout << &num << endl;
    // cout << *p << endl;

    // size_t size = 0;
    // double* temp_ptr = new double[size];

    // cout << "how many temo? ";
    // cin>>size;

    // while (true) {
    //     temp_ptr = new double[size];
    // }
    
    // cout << temp_ptr << endl;

    // delete [] temp_ptr;
    

    // int i = 90;


    // int* ptr = nullptr;

    // ptr = &i;

    // cout << i << endl;
    // cout << &i << endl;

    // cout << ptr << endl;
    // cout << *ptr << endl;
    
    // *ptr = 98;


    // cout << *ptr << endl;
    // cout << i << endl;


    // int i[] = { 0, 1, 2, 3, 4, 5, 6, 7};

    // int* array_ptr = nullptr;

    // array_ptr = i;


    // for (size_t i = 0; i < 8; i++)
    // {
    //     cout << array_ptr[i] << endl;
    // }
    

    // int* i = new int;

    // *i = 90;

    // cout << *i << endl;
    // cout << i << endl;


    // delete i;


    // int* i = new int[9];

    // i[0] = 90;
    // i[1] = 101;
    // cout << *(i + 1) << endl;
    // delete[] i;


    // string name = "Manveer Singh";


    // string your_name = " Sakshi";


    // cout << name + your_name << endl;


    int yo[] = { 0, 1, 2, 3, 4, 5};


    int* score_ptr = yo;
    for (int i = 0; i < 6; i++)
    {
        cout << *score_ptr++ << endl;
        // score_ptr++;
    }
    
    return 0;
}