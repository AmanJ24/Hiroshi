#include <SFML/Graphics.hpp>
#include <iostream>


int main(){
    sf::RenderWindow window(sf::VideoMode(600,600),"Over-powered", sf::Style::Default);
    
    while(window.isOpen()){

        sf::Event evnt;
        while(window.pollEvent(evnt)){

            if(evnt.type == sf::Event::Closed){
                window.close();
            }
        }
    }
}