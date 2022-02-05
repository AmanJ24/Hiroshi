#include <iostream>
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <SFML/Window.hpp>
#include <SFML/Audio.hpp>
#include <SFML/Network.hpp>

using namespace std;
int main()
{
    sf::RenderWindow window(sf::VideoMode(600, 600), "My first game", sf::Style::Titlebar | sf::Style::Close);
    sf::Event event;

    //game loop;
    while(window.isOpen()){

        while(window.pollEvent(event)){
            switch(event.type){
                case sf::Event::Closed:
                    cout<< "This is called" << endl;
                    window.close();
                    break;
                case sf::Event::KeyPressed:
                    if(event.key.code == sf::Keyboard::Escape)
                        window.close();
                    break;
            }
        }
    }

    //update 
    window.clear(sf::Color::Blue);   

    window.display();
    return 0;
}