#include <iostream>
#include "second.h"
using namespace std;


int main(){
   char yes;
   int how_many= 0;
   string name = "nothing";

   cout << "You don't have any choice " << name << "you have to watch anime" << endl;
   cout << "you have only 6 choices" << endl;
   Player::display();

   do{
      cout << "If you don't want to watch anime then press N , and if you want to watch anime then press Y: ";
      cin>>yes;
      if(yes == 'y')
      {
         cout << "nice " << endl;
      }
      else if (how_many == 5){
         cout << "Fuck you " << endl;
      }
      else if(how_many == 6){
         cout << "Nice so you are going to watch anime now nice " << endl;
         Player::display();
      }
      else if(how_many >= 10) {
         cout << "You have to watch anime" << endl;
      }
      how_many += 1;
   }while(yes != 'y' && yes != 'Y');
   return 0;
}