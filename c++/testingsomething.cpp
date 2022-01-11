#include <iostream>
#include <time.h>
#include <vector>

using namespace std;


void arrayf(int* );
int main(){

    // srand(time(NULL));
    // int random_number;
    // for (int i = 0; i < 5; i++)
    // {
    //     random_number = (rand() % 6) + 1;
    //     cout << random_number << endl;
    // }

    // int size = 0;
    // cin >> size;
    // int* ptr = new int[size];
    
    // for (int i = 0; i < size; i++)
    // {
    //     cin>>ptr[i];
    //     ptr[i];
    // }

    // for (int i = 0; i < size; i++)
    // {
    //     cout << ptr[i] << endl;
    // }
    
    // delete [] ptr;

//     vector <vector<int>> hello
//     {
//         {1,     2,      3},
//         {4,     5,      6},
//         {7,     8,      9},
//     };


    // int arra[3][3]
    // {
    //     {1, 2, 3},
    //     {4, 5, 6},
    //     {7, 8, 9},
    // };
    // arrayf(arra);
    
    int arr[1][4] ={5,7,8,9};
    //int* x = arr;

    // cout << arr << endl;
    // arrayf((int*)arr);


    std::find(7,arr);
    return 0;
}


// int arrayf(int* x[][3])
// {
//     cout << "Hello World" << endl;
// }