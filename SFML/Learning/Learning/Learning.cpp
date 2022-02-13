#include <SFML/Graphics.hpp>

int main()
{
    sf::RenderWindow window(sf::VideoMode(600, 600), "Over-powered", sf::Style::Default | sf::Style::Resize);

    while (window.isOpen()) {
        
        sf::Event evnt;
        while (window.pollEvent(evnt)) {
            switch (evnt.type) {
            case sf::Event::Closed:
                window.close();
            }
        }
    }
    return 0;
}


