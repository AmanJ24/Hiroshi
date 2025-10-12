#include <iostream>
using namespace std;

class Rectangle {
    private:
        int length;
        int width;

    public:
        Rectangle(int l, int w): length(l), width(w) {}

        friend int calculateArea(Rectangle rect);
        friend void showDetails(Rectangle rect);
};

int calculateArea(Rectangle rect){
    return rect.length * rect.width;
}

void showDetails(Rectangle rect){
    cout << "length: " << rect.length << " " << "width: " << rect.width << endl;
}

int main(){
    Rectangle rect(10, 5);

    cout << "Area of Rectangle: " << calculateArea(rect) << endl;

    showDetails(rect);

    return 0;
}
