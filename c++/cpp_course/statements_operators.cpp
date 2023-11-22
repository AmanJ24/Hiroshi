#include <iostream>

/*Expressions - examples 
 * 34 			//literal
 * int favourite_number //variable
 * 1 + 5  		//addition
 * 2 * 5 		//multiplication
 * a > b 		//relational
 * a = b 		//assignment
 * */



/*Statements - examples 
 * int x; 		//declaration
 * favourite_number = 12; //assignment
 * 1 + 5;		//expression
 * x = 2 * 5;		assignment
 * if(a > b) std::cout << "a is greater than be"; //if
 * */



int main(){
	int num_1 {10};
	int num_2 = num_1 = 100; //the value will be 100 of num1 and num2 , because assignment works from right to left;
	std::cout << num_1 << " , " << num_2 << std::endl;

	/*----------------------Arithmetic Operators----------------------------*/
	/*
	  + addition
	  * Multiplication
	  / division
	  % modulor or reminder (works only with integers)

	  + , - , * and / operators are overloaded to work with multiple types such as int , double etc
	  % only for integers  types
	 */

	std::cout << num_1 << " + " << num_2 << " = " << num_1 + num_2 << std::endl;
	std::cout << num_1 << " - " << num_2 << " = " << num_1 - num_2 << std::endl;
	std::cout << num_1 << " * " << num_2 << " = " << num_1 * num_2 << std::endl;
	std::cout << num_1 << " / " << num_2 << " = " << num_1 / num_2 << std::endl;
	std::cout << num_1 << " % " << num_2 << " = " << num_1 % num_2 << std::endl;


	int be_aware = 200 / 100; //answer will not be 0.5 because it is int
	
	std::cout << 4.4 / 2 << std::endl;  //c++ convert the type if it can like this
	
	//Mixed Type Expressions
	//lower op higher 		the lower is promoted to a higher
	std::cout << 2 * 5.2 << std::endl;
	//lower = higher; the higher is demoted to a lower
	int num {0};
	num = std::static_cast<int>(100.2); //.2 is data loss
	

	/*------------------------------Increment Decrement-------------------------*/
	/*Increment operator --> ++
	  Decrement operator --> --

	  Prefix ++num
	  postfix num++

	  ALERT!! Never use it twice for the same variable in the same statement!!
	 
	 */

	
	int number = 1;

	int number_2 = ++number + 2; //  the result will be 4;
	//int number_2 = number++ + 2; //  the result will be 3;
	std::cout << number_2 << std::endl;


	/*--------------------------Explicit type casting---------------------------*/
	int total_amount {100};
	int total_number {8};
	double average {0.0};

	average = total_amount / total_number;
	std::cout << average << std::endl; // result will be 12 not 12.5
	average = 0.0;
	
	average = static_cast<double>(total_amount) / total_number;
	std::cout << average << std::endl;


	/*------------------------Equality operators----------------------*/
	// The == and != operators
	// to get true false instead of 0 and 1 use boolalpha
	std::cout << std::boolalpha;
	std::cout << (100 == 100) << std::endl;
	std::cout << (100 != 100) << std::endl;

	/*------------------------Relation operators-------------------------*/
	/*operator 				Meaning
	 * >					greater than 
	 * >=					greater than or equal to
	 * <					less than 
	 * <= 					less than or equal to 
	 * <=>					three way comparison (C++20)
	<=> --> This operator compares two expressions and evaluates to zero if they are equal , less than zero if the left hand side is greater and greater than zero if the right hand side is greater than the left hand side;
	* */

	/*---------------------------Logical operators--------------------------*/
	/*Operator				Meaning
	 * not or !				negation
	 * and or && 				logical and
	 * || or or				logical or
	* */

	//Examples 
	std::cout << (8 == 8 && 7==7) << std::endl;
	std::cout << (8 == 8 || 7==6) << std::endl;
	std::cout << !(8 == 8 && 7==6) << std::endl;
	
	//precedence in logical operators are 1. not operator or ! , 2. && operator or and , 3. or or || operator
	/*-------------------short circuit Evaluation----------------------------*/
	//expr1 && expr2 && expr3 --> if one is false than output will be false
	//expr1 || expr2 || expr3 --> if one is true than output will be true 
	
	/*----------------------------Compound Assignment--------------------------*/
	/*
		operator		example			Meaning
		+=			lhs += rhs;		lhs = lhs + (rhs);
		-=			lhs -= rhs;		lhs = lhs - (rhs);
		*=			lhs *= rhs;		lhs = lhs * (rhs);
		/=			lhs /= rhs;		lhs = lhs / (rhs);
		%=			lhs %= rhs;		lhs = lhs % rhs;
		>>=			lhs >>= rhs;		lhs = lhs >> (rhs);
		<<=			lhs <<= rhs;		lhs = lhs << (rhs);
		&= 			lhs &= rhs;		lhs = lhs & (rhs);
		^= 			lhs ^= rhs;		lhs = lhs ^ (rhs);
		!= 			lhs != rhs;		lhs = lhs ! (rhs);
	*/

	return 0;
}
