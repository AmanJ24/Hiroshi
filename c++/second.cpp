#include "second.h"
#include <iostream>
#include <vector>


std::vector <std::vector<int>> Player::something{
    {1,2,3,4},
    {5,6,7,8}
};
std::vector<std::string> Player::anime_name{
    {"1. My dress_up darling"},
    {"2. Naruto"},
    {"3. Demon slayer"},
    {"4. High school dxd - you will like this one"},
    {"4. Dragon ball"},
    {"6. One piece"}
};



void Player::display(){
    for (int i = 0; i <anime_name.size(); i++)
    {
       std::cout << anime_name[i] << std::endl;
    }
    
}