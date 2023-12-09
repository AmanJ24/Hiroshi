#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <vector>



/*
	example that if you use function overloading and initialize them with default value compiler can get confuse betweeen int print and double print like this 
	print(int = 100);
	print(double = 213.23);


	and when you use this function in int main function it will give you error because it can't decide which one to use 


		other Things
		float will be upgraded to double if you have double overloaded function 
		char is consider as integer so print(int = 100) <-- this function will be called
  */



int add_number(int first_number , int second_number); // provide parameter name too for documentation purpose or ease to understand code purpose
size_t add_number(size_t first_number, size_t second_number);
void function();
void say_hello(std::string);
void vector_loop(std::vector<int> size);




//we can give default values to functions
//and we can define function first with default value and when we will write code in it we don't need to write the default value like this 

//you only need to define default value one time in any fucntion declaration you will do;
double complete_cost(double value , double tax = 18);
double complete_cost(double value , double tax){

	return value + ((tax / 100) * value);
}



double tax_reducer(double complete_cost , double tax_rate){
	return (tax_rate / 100) * complete_cost;
}





/* ------------------------------------Overloading Fucntions------------------------ */
int subtract_number(int first_number , int second_number);
float subtract_number(float first_number , float second_number);



int subtract_number(int first_number , int second_number){
	std::cout << "INT one is called" << std::endl;;
	return first_number - second_number;
}
float subtract_number(float first_number , float second_number){
	std::cout << "float one is called" << std::endl;;
	return first_number - second_number;
}



/* --------------------------passing arrays through functions ------------------------- */
//you can do like this in parameters int array_size = sizeof(array) / 4;
//we can tell compiler that you can't change the array which we are passing through  by using const
void array_count(const int array [] , size_t array_size){
	for(int i = 0; i < array_size; i++){
		std::cout << array[i] << std::endl;
	}
}



/* -------------------------------------using pointers to actually change the value ---------------------------------------- */
void change_number_to_100(int* num){
	*num = 100;
	return;
}


void print(const std::vector<int>* v){
	for(int s : *v){
		std::cout << s << std::endl;
	}
}


/* ---------------------------------------Static local variables------------------- */
static int loop_count = 0;
void how_many_time_loop(){
	loop_count++;
	std::cout << loop_count << std::endl;
	return;
}

int main(){

	std::cout << std::sqrt(3425) << std::endl;
	std::cout << std::cbrt(23) << std::endl;
	std::cout << std::pow(2.0,3.0) << std::endl;
	std::cout << add_number(static_cast<size_t>(100), static_cast<size_t>(100)) << std::endl; //this is to call size_t function
	std::cout << add_number(100 , 100) << std::endl; //this will automatically call integer because they are int type and compile prefer it first;
	/* std::cout << funciton() << std::endl; you can't do this because , you haven't defined what it will do like you have defined add_number function even if its int or double type function */
	say_hello("Hello World");
	std::cout << complete_cost(20) << std::endl;
	std::cout << tax_reducer(38'500, 12) << std::endl;
	int random_number = 100;
	float random_number_1 = 23.023f;
	
	std::cout << subtract_number(random_number , random_number) << std::endl;
	std::cout << subtract_number(random_number_1 , random_number_1) << std::endl;

	//this program will produce random numbers
	/* std::srand(std::time(0)); //time only take 0 or nullptr as argument or else it will create an error */
	/* for(int i = 0; i < 20; i++){ */
	/* 	std::cout << std::rand() % 20 + 0 << std::endl; */
	/* } */
	std::vector<int> for_loop(100 , 23);
	vector_loop(for_loop);
	print(&for_loop); // you can also do like this by passing the address of the vector instead of the copy but make sure to use const 
	int array_loop [] = {1,2,3,4,5,6};
	int array_size = sizeof(array_loop) / 4;
	array_count(array_loop , array_size);
	int number {0};
	change_number_to_100(&number);
	std::cout << number << std::endl;
	std::cout << "HELLO WORLD" << std::endl;
	
	//static variable test
	how_many_time_loop();
	how_many_time_loop();
	std::cout << "HELLO WORLD" << std::endl;
	return 0;
}



void vector_loop(std::vector<int> size){
	for(int s : size){
		std::cout << s << std::endl;
	}
}


//if you are using INT instead of SIZE_T then 
int add_number(int first_number , int second_number){
	std::cout << "integer one" << std::endl;
	if(first_number < 0 || second_number < 0){
		return 0;
	}
	return first_number + second_number;
}


//writing function to add number; --> learning purpose
size_t add_number(size_t first_number , size_t second_number){
	std::cout << "size_t one" << std::endl;
	return first_number + second_number;
}


void say_hello(std::string user_will_say_hello){
	std::cout << user_will_say_hello << std::endl;
	return;
}
