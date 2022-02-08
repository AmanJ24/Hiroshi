#include <SFML/Graphics.hpp>
#include <iostream>


int main(){
    sf::RenderWindow window(sf::VideoMode(600,600), "Over-Powered", sf::Style::Default | sf::Style::Titlebar | sf::Style::Resize);
    sf::RectangleShape player(sf::Vector2f(100.0f, 100.0f));
    player.setFillColor(sf::Color::Blue);
    player.setOrigin(50.0f, 50.0f);

    while(window.isOpen()){

        sf::Event evnt;
        while(window.pollEvent(evnt)){
            switch(evnt.type){
                case sf::Event::Closed:
                    window.close();
                    break;
            }
        }

        
        if(sf::Keyboard::isKeyPressed(sf::Keyboard::Key::A)){
            player.move(-0.1f,0.0f);
        }
        if(sf::Keyboard::isKeyPressed(sf::Keyboard::Key::D)){
            player.move(0.1f,0.0f);
        }
        if(sf::Keyboard::isKeyPressed(sf::Keyboard::Key::W)){
            player.move(0.0f,-0.1f);
        }
        if(sf::Keyboard::isKeyPressed(sf::Keyboard::Key::S)){
            player.move(0.0f,0.1f);
        }

        if(sf::Mouse::isButtonPressed(sf::Mouse::Left)){
            sf::Vector2i mouse_pos = sf::Mouse::getPosition(window);
            player.setPosition(float(mouse_pos.x), float(mouse_pos.y));
        }

        window.clear();
        window.draw(player);
        window.display();
    }
}