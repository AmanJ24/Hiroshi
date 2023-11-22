#include <iostream>
#include <string>



int main(){
	std::string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	std::string key = "vnjsjdfsjfwerowievrnowiebriewpqwierxmqpwoerwevrioewovn"; 


	std::cout << "Enter your password with no space which i will encrypt: ";
	std::string password;
	std::getline(std::cin,password);


	
	std::string temp_password = password;
	for(int i=0; i < password.length(); i++)
	{
		for(int j=0; j < alphabet.length(); j++)
		{
			if(password[i] == alphabet[j])
			{
				password[i] = key[j];
				break;
			}
	
		}
	}


	std::cout << "--------------------------------------------" << std::endl;
	//to decrypt this encrypted password
	std::string decrypted_password;
	for(int i = 0; i < password.length(); i++){
		for(int j = 0; j < key.length(); j++){
			if(password[i] == key[j]){
				break;
			}
		}
	}

	std::cout << "encrypted password: " << password << std::endl;
	std::cout << "decrypted password: " << decrypted_password << std::endl;

    /* cout << "This is your encrypted password: "<< password << endl; */
    /* password = temp_password; */
    /* cout << "And this is your dcrypt password: "<<password << endl; */
    return 0;
}
