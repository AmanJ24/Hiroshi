#include <iostream>
#include <string>
#include <cctype> //--> this library to perform string things i don't know about
#include <cstring>


int main(){
	char c {'A'};
	/*--------------------------------Testing characters--------------------*/
	/*
	isalpha(c); // True if c is a letter
	isalnum(c); // True if c is a letter or digit 
	isdigit(c); // True if c is a digit 
	islower(c); // True if c is lowercase letter
	isprint(c); // True if c is a printable character
	ispunct(c); //True if c is a punctuation character
	isupper(c); // True if c is an uppercase letter
	isspace(c); // True if c is whitespace
	*/

	if(isupper(c)){
		std::cout << "Hello world" << std::endl;
	}
	else{
		std::cout << "nothing" << std::endl;
	}
	
	
	
	/*-------------------------Converstion Functions-------------------*/
	// tolower(c)			return lowercase of c
	// toupper(c)			return uppercase of c
	
	std::cout << static_cast<char>(toupper(c)) << std::endl;
	std::cout << static_cast<char>(tolower(c)) << std::endl;
	
	
	/*-------------------C Style strings--------------------*/
	
	char string[] {"c++ is fun"};
	std::cout << string << std::endl;
	//we can do this to get the size of c style string 
	//, there are two ways
	std::cout << strlen(string) << std::endl;
	std::cout << sizeof(string) - 1 << std::endl;
	
	
	char my_name[80];
	
	//my_name = {"Manveer"}; --> This is wrong way of doing it;
	strcpy(my_name , "Manveer");
	strcat(my_name , " Singh");
	std::cout << strcmp(my_name , "Manveer Singh") << std::endl;
	std::cout << strlen(my_name) << std::endl;
	std::cout << my_name << std::endl;
	
	
	char first_name[100];
	char last_name[100];
	
	/* std::cout << "Enter your first Name:  "; */
	/* std::cin.getline(first_name , sizeof(first_name)); */
	/* std::cout << "Enter your last Name:  "; */
	/* std::cin.getline(last_name, sizeof(last_name)); */
	/* std::cout << std::endl; */
	
	strcat(first_name , last_name);
	std::cout << first_name << std::endl;
	
	/*  */
	/* std::string user_name; */
	/* std::cout << "Enter your user_name again" << std::endl; */
	/* std::getline(std::cin , user_name); */
	/* std::cout << user_name << std::endl; */






	/*-------------------C++ Strings-------------------------------------*/
	/*
	 std::string s1; 	//Empty
	 std::string s2 {"Frannk"};	// Frank
	 std::string s5 {s2};		//Frank
	 std::string s4 {"Frank" , 3};  //fra
	 std::string s5 {s3 , 0 , 2}; 	//Fr
	 std::string s6 (3 , 'X');	//XXX
	 */

	/*------------------------Assignment--------------------------------*/
	std::string s_1 {"C++ Rocks!"};
	std::string s_2 {"Hello"};
	s_2 = s_1;


	//Concatenation
	

	//Right way to do it
	std::string part_1 {"C++"};
	std::string part_2 {"is a powerful"};


	std::string sentence;

	sentence = part_1 + " " + part_2 + " language"; //right way to do it;
	
	//sentence = "C++ " + " is powerful language"; //wrong way to do it 
	//But we can do this;
	
	//because c style string and c++ string can add together;
	sentence = "C ++ " + part_2;
	std::cout << sentence << std::endl;

	//You can change specific character in c++ std::string;
	
	std::string user_name {"manveer"};
	std::cout << user_name << std::endl;
	user_name.at(0) = 'M';
	std::cout << user_name << std::endl;


	for(char c : user_name){
		std::cout << c << std::endl;
	}

	//this will print ascci value 
	for(int c : user_name){
		std::cout << c;
	}
	std::cout << std::endl;


	//You can use comparison operators  like you do simple
	
	/*--------------------------Substrings--------------------------*/

	//substr(starting index , length);
	std::cout << user_name.substr(0,4) << std::endl;
	std::cout << user_name.erase(0,1) << std::endl;
	size_t position = user_name.find("anveer");

	if(position != std::string::npos){
		std::cout << user_name.at(position) << std::endl;
	}
	else{
		std::cout << "Not found" << std::endl;
	}

	return 0;
}
