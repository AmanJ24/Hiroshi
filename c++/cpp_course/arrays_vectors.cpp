#include <iostream>
#include <vector>

/*Declaring the array 
 * Element_name array_name [constant number of element]; 
 *
 *Initialization 
 *Element_name array_name [constant number of element] {init list}
 * */

int main(){
	/*-----------------------------------Raw Arrays-----------------------------*/
	//Declaring 
	int test_score [5]; 
	const int days_in_year [3] {365 , 2 , 23}; //you can't change these elements
	

	//Initialization
	int test_score_1 [5] {1,2,3,4,5};
	int another_array_1 [] {1,2,3,4,5,6}; //size automatically calculated
	int high_score_per_level [10] {3,5}; //init to 3,5 and remaining to 0
	

	/*-------------------------Accessing array elements------------------------*/
	//array_name [element_index]; like --> test_score[1];
	std::cout << test_score_1[0] << std::endl;
	std::cout << test_score_1[1] << std::endl;
	std::cout << test_score_1[2] << std::endl;
	std::cout << test_score_1[3] << std::endl;
	std::cout << test_score_1[4] << std::endl;

	/*---------------------------changin the contents of array elements---------*/
	test_score_1[0] = 100;
	std::cout << test_score_1[0] << std::endl;


	/*-------------------------Multidimensional Arrays and Vector--------------------------*/
	//Element_Type array_name [dim1_size] [dim2_size];
	int movie_rating[3][4]{
		{1,2,3,4},
		{5,6,7,8},
		{9,10,11,12}
	};

	//just for loop example
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 4; j++){
			std::cout << movie_rating[i][j] << " ";
		}
		std::cout << std::endl;
	}


	std::vector< std::vector<int>> movie_rating_vector {
		{1 , 2 , 3},
		{4 , 5 , 6},
		{7 , 8 , 9}
	};
	//one way to access it 
	std::cout << movie_rating_vector.at(0).at(0) << std::endl;
	//another way to access it is raw array method
	std::cout << movie_rating_vector[0][0] << std::endl;
	
	/*---------------------------------VECTORS---------------------------------*/
	//DECLARING VECTOR --> use constructor initialization 'cause its an object bruh
	std::vector<int> test_score_2 (3);
	std::vector<char> vowels (4);

	//Initializing 
	std::vector<char> vowels_1 {'a', 'b' , 'c' , 'd'};
	std::vector<int> test_score_22 {100,98,89};
	std::vector<int> temperature(100 , 80); // (size , declare them all)
	
	//we can access vectors using at mothod 
	std::cout << test_score_2.at(0) << std::endl;
	//assigning using at method
	test_score_2.at(0) = 100;
	std::cout << test_score_2.at(0) << std::endl;

	//push back method in vectors
	test_score_2.push_back(100);
	std::cout << test_score_2.at(test_score_2.size() - 1) << std::endl;


	int number = 0;
	std::vector<int> user_value;
	std::cin >> number;
	user_value.push_back(number);
	user_value.clear(); //this clear all the vector value
	std::cout << user_value.at(0) << std::endl;
	return 0;
}
