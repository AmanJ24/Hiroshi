#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	cout << "Enter an amount in rupees: ";
	float how_much_rupees;
	cin>>how_much_rupees;


	float rupees_in_yen = (how_much_rupees * 1.52f);
	float rupees_in_dollar = (how_much_rupees * 0.013f);
	float rupees_in_euro = (how_much_rupees * 0.012f);
	float rupees_in_Hungarian_forint = (how_much_rupees * 4.33f);


	cout << "Rupees in Dollar: " << rupees_in_dollar << endl;
	cout << "Rupees in Yen: "<<rupees_in_yen << endl;
	cout << "Rupees in Euro: "<<rupees_in_euro << endl;
	cout << "Rupees in Hungarian Forint: "<<rupees_in_Hungarian_forint << endl;

	cout << "This is working" << endl;
	return 0;
}
