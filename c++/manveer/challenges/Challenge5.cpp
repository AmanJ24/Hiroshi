#include <iostream>



using namespace std;

int print(int* array, int array_size);
int* apply_all(int const* array, int array_size, int const* array2, int array2_size);

int main(){

    const int array1_size = 5;
    const int array2_size = 3;

    int array1[] = {1,2,3,4,5};
    int array2[] = {10,20,30};

    cout << "Array 1: ";
    print(array1,array1_size);


    cout << "Array 2: ";
    print(array2,array2_size);

    int* result = apply_all(array1,array1_size, array2,array2_size);
    size_t result_size = array1_size * array2_size;

    cout << "Result: ";
    print(result,result_size);

    cout<<endl;
}

int print(int* array, int array_size)
{
    cout << "[";
    for (int i = 0; i < array_size; i++)
    {
        cout << " " << *(array + i);
    }
    cout << " ]";
    
}


int* apply_all(int const * array, int array_size, int const* array2, int array2_size)
{
    int* result = new int[array_size * array2_size];

    int position = 0;
    for (int i = 0; i < array_size; i++)
    {
        for (int i = 0; i < array2_size; i++)
        {
            result[position] = (array[i] * array2[i]);
            position++;
        }
        
    }
    
    return result;
    
}