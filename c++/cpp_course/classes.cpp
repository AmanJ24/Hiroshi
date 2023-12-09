#include <iostream>

class Base
{
public:
};

class Derived : public Base
{
public:
    void say_hello()
    {
        std::cout << "Hello world" << std::endl;
        return;
    }
};

int main()
{
    Derived object;
    object.say_hello();
}