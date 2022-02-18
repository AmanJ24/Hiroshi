#include <iostream>
#include <fstream>


int main(){
   std::ifstream in_file;
   in_file.open("hello.txt");
   std::string line;

   if(!(in_file.is_open())){
      std::cout << "This is not open" << std::endl;
   }
   else{
      std::cout << "This is not working" << std::endl;
   }
   return 0;
}