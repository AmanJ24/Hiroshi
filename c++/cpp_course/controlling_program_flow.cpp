#include <iostream>
#include <vector>

/*if Statement
 * if(parameters){
 * 	statement
 * }
 * else if{
 *
 * }
 * else{
 *
 * }
 * */



/*Switch statement
 * switch(parameter){
 * 	case expression_1: statement;
 * 		break;
 * 	case expression_2: statement;
 * 		break;
 * 	default: statement;
 * }
 * */



//this is conditional statement (i guess :);
int real_number(int value){
	return value > 100 ? 1 : 0;
}


int main(int argv , char* argc[]){
	union money{
		int rice;
		float rupees;
	};

	union money m1;
	m1.rice = 32;
	m1.rupees = 4.56f;
	std::cout << m1.rupees<< std::endl;
	std::cout << real_number(100) << std::endl; 
	//initializing variables to use it in if statement
	char selection {'A'};
	int num {10}, health{90};
	bool player_healed {true};


	/*------------------------if statement----------------*/
	if(selection == 'A'){
		std::cout << "You selected A" << std::endl;
	}
	if(num >= 10){
		std::cout << "num is greater than 10" << std::endl;
	}
	if(health < 100 && player_healed){
		health = 100;
		std::cout << health << std::endl;
	}

	/*------------------------if else statement---------------------*/
	if(num > 10){
		std::cout << "nice" << std::endl;
	}
	else if(num == 10){
		std::cout << "same" << std::endl;
	}
	else{
		std::cout << "not nice" << std::endl;
	}

	/*----------------------Nested if statement------------------------*/
	if(num >= 10){
		if(health == 100){
			std::cout << "This is nested statement" << std::endl;
		}
		else{
			std::cout << "else statement" << std::endl;
		}
	}


	/*-----------------------Switch statement------------------------------*/
	switch (num) {
		case 1: std::cout << "Hello" << std::endl;
		case 3: std::cout << "HELLO" << std::endl;
		break;
		case 2: std::cout << "World" << std::endl;
		break;
		default: std::cout << "Hello world" << std::endl;
	}

	/*-------------------------Iteration--------------------------------------*/
	//for loop
	for(int i {0}; i < 10; i++){
		if(i % 2 == 0 && i > 0){
			std::cout << i << " ";
		}
	};
	
	std::cout << std::endl;
	int scores[] {1,2,3,4,5};

	for(int i = 0; i < 5; i++){
		std::cout << scores[i] << " ";
	}
	std::cout << std::endl;

	//comma operator
	for(int i {0} , j {2}; i <= 5; i++ , j++){
		std::cout << " " <<  i << " " << j;
	}
	std::cout << std::endl;


	for(int i = 0; i < 10; i++){
		for(int j = 0; j < 10; j++){
			std::cout << i <<  " " << j;
		}
		std::cout << std::endl;
	}

	/*---------------------Endless loop-------------------------------*/
	for(;;){
		std::cout << "Endless loop" << std::endl;
		break; // --> remove this to get infinite loop
	}



	/*------------------------for range-based loop-------------------------*/

	std::vector<int> for_range_loop {1,2,3,4,5,6,7,8,9,10};

	//we can use auto to simplify things
	std::cout << "with auto keyword" << std::endl;
	for(auto loop : for_range_loop){
		std::cout << loop << " ";
	}

	std::cout << std::endl;
	std::cout << "without auto keyword" << std::endl;
	for(int loop : for_range_loop){
		std::cout << loop << " ";
	}
	std::cout << std::endl;

	//we can also do this 
	for(int loop : {1 ,2 ,3 ,4 ,5}){
		std::cout << loop << " ";
	}

	char character[] = "Hello world";
	int length = sizeof(character) - 1;
	for(int i = 0; i < length; i++){
		std::cout << character[i];
	}
	std::cout << std::endl;




	/*-----------------------------While Loop------------------------------*/
	int large_value {0};
	while(large_value < 100){
		int i = 1;
		i++;
		large_value += i;
	}
	std::cout << large_value << std::endl;


	/*----------------------------Do-While loop------------------------------*/
	bool is_do_while = true;
	do{
		std::cout <<"THIS IS DO WHILE LOOP" << std::endl;
		is_do_while = false;
	}while(is_do_while);

	return 0;
}




