"""
1 
1 2 
1   3 
1     4 
1 2 3 4 5 
"""
def hollow_number_pyramid(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            if j in [1, i] or i == num:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print("")

#-----------------------------------------------------------#

'''
1 2 3 4 5 6 
1       5 
1     4 
1   3 
1 2 
1
'''
def hollow_inverted_number_pyramid(num):
    for i in range(num+1, 1, -1):
        for j in range(1, i):
            if j in [1, i-1] or i-1 == num:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print("")

#-----------------------------------------------------------#

'''
1 2 3 4 5 6 
2       6
3     6
4   6
5 6
6
'''
def hollow_upside_down_pyramid(num):
    for i in range(num+1, 1, -1):
        for j in range(1, i):
            if j == 1:
                print(num-i+2, end=" ")
            elif i-1 == num:
                print(j, end=" ")
            elif j == i-1:
                print(num, end=" ")
            else:
                print(" ", end=" ")
        print("")

#-----------------------------------------------------------#

'''
         1 
       1 2 1
     1 2 3 2 1
   1 2 3 4 3 2 1
 1 2 3 4 5 4 3 2 1
'''
def numeric_palindrome_equilateral_pyramid(num):
    for i in range(1, (num*2)+1, 2):
        for j in range((num*2) - i):
            print("", end=" ")
        for k in range(1, i+1):
            if k <= i//2:
                print(k, end=" ")
            else:
                print(i-k+1, end=" ")
        print("")

#-----------------------------------------------------------#

'''
* 
* *
* * *
* * * *
* * *
* *
*
'''
def solid_half_diamond(num):
    val = -2
    for i in range(1, num+2):
        if i <= (num//2)+1:
            for j in range(i):
                print("*", end=" ")
            print("")
        else:
            val += 1
            for j in range((num//2)-val, 1, -1):
                print("*", end=" ")
            print("")

#-----------------------------------------------------------#

'''
*********1**********
********2*2*********
*******3*3*3********
******4*4*4*4*******
*****5*5*5*5*5******
'''
def fancy_pattern(num):
    for i in range(1, num+1):
        for j in range((num*2)-i):
            print("*", end="")
        for j in range(1, i+1):
            print(i, end="*")
        for j in range((num*2)-i):
            print("*", end="")
        print("")

#-----------------------------------------------------------#

def fancy_pattern_2(num):
    val = 1
    for i in range(num):
        for j in range(1, 2*i+2):
            if j & 1:
                print(val, end="")
                val += 1
            else:
                print("*", end="")
        print("")

    new = 0
    for i in range(num-1, -1, -1):
        new = val-i-1
        for j in range(2*(i-1)+3, 0, -1):
            if j & 1:
                print(val-i-1, end="")
                val += 1
            else:
                print("*", end="")
        val = new
        print("")

                

#--------------TESTS--------------------#
# hollow_number_pyramid(5)
# hollow_inverted_number_pyramid(6)
# hollow_upside_down_pyramid(6)
# numeric_palindrome_equilateral_pyramid(5)
# solid_half_diamond(6)
# fancy_pattern(5)
# fancy_pattern_2(4)