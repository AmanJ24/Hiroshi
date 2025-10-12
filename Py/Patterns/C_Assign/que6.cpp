#include <iostream>
using namespace std;

class Student {
private:
    string name;
    int age;
    float m1, m2, m3, avg;
    string phone;

public:
    // Method to input data
    void getdata() {
        cout << "Enter name: ";
        cin >> name;
        cout << "Enter age: ";
        cin >> age;
        cout << "Enter marks for subject 1: ";
        cin >> m1;
        cout << "Enter marks for subject 2: ";
        cin >> m2;
        cout << "Enter marks for subject 3: ";
        cin >> m3;
        cout << "Enter phone number: ";
        cin >> phone;
        
        // Calculate average
        avg = (m1 + m2 + m3) / 3;
    }

    // Method to display data
    void showdata() {
        cout << "\nStudent Details:\n" << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Marks 1: " << m1 << endl;
        cout << "Marks 2: " << m2 << endl;
        cout << "Marks 3: " << m3 << endl;
        cout << "Average: " << avg << endl;
        cout << "Phone: " << phone << endl;
    }
};

int main() {
    Student s;
    s.getdata(); 
    s.showdata();
    return 0;
}
