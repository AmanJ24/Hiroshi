#include <iostream>
#include <fstream>


int main(){

   std::ofstream in("hello.txt");
   in<<"How are you doing!";
   std::cout << "Hello, World" << std::endl;
   return 0;
}