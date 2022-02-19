#include <SFML/Graphics.hpp>
#include <iostream>


int main(){
    sf::RenderWindow window(sf::VideoMode(600,600), "Manveer-Singh", sf::Style::Default | sf::Style::Resize | sf::Style::Titlebar);
    sf::RectangleShape player(sf::Vector2f(100,100));
    player.setFillColor(sf::Color::Blue);
    player.setOrigin(50,50);
    while(window.isOpen()){

        sf::Event evnt;
        while(window.pollEvent(evnt)){
            switch(evnt.type){
                case sf::Event::Closed:
                    window.close();
                    break;
                case sf::Event::Resized:
                    std::cout << evnt.size.height << "x" << evnt.size.width << std::endl;
                    break;
            }
        }

        if(sf::Mouse::isButtonPressed(sf::Mouse::Button::Left)){
            sf::Vector2i mouse_pos = sf::Mouse::getPosition(window);
            player.setPosition(static_cast<float>(mouse_pos.x), static_cast<float>(mouse_pos.y));
        }
        window.clear();
        window.draw(player);
        window.display();
    }
}