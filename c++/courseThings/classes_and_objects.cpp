#include <iostream>

using namespace std;


int* y = new int;

class Program{

	Program(){
		cout << "This one is called" << endl;
	}

	//Program
};
void trying(int &num)
{
	cout << "This is your entered number: " << num << endl;
	*y = num;
	cout << y << endl;
	cout << *y << endl;
}

