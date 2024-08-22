## RIGHT HALF PYRAMID PATTERN
def right_half_pyramid(num):
    for i in range(1, num):
        for j in range(i):
            print("* ", end='')
        print("")

#----------------------------------------------------------#

## LEFT HALF PYRAMID PATTERN
def left_half_pyramid(num):
    for i in range(1, num+1):
        for j in range(num-i):
            print("  ", end='')
        for k in range(i):
            print("* ", end='')
        print("")

#----------------------------------------------------------#

## FULL PYRAMID PATTERN
def full_pyramid(num):
    for i in range(1, num+1):
        for j in range(num-i):
            print(" ", end='')
        for k in range(i):
            print("* ", end='')
        print("")

#----------------------------------------------------------#

## INVERTED RIGHT HALF PYRAMID
def inverted_right_half_pyramid(num):
    for i in range(num):
        for j in range(num-i):
            print("* ", end="")
        print("")

#----------------------------------------------------------#

## INVERTED LEFT HALF PYRAMID 
def inverted_left_half_pyramid(num):
    for i in range(num):
        for j in range(i):
            print("  ", end="")
        for k in range(num-i):
            print("* ", end="")
        print("")

#----------------------------------------------------------#

## INVERTED FULL PYRAMID
def inverted_full_pyramid(num):
    for i in range(num):
        for j in range(i):
            print(" ", end="")
        for k in range(num-i):
            print("* ", end="")
        print("")

#----------------------------------------------------------#

## RHOMBUS PATTERN 
def rhombus_pattern(num):
    for i in range(num):
        for j in range(i):
            print(" ", end="")
        for k in range(num):
            print("* ", end="")
        print("")

#----------------------------------------------------------#

## DIAMOND PATTERN
def diamond_pattern(num):
    for i in range(1, (num//2)+1):
        for j in range((num//2) - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print("")
        
    for i in range(1, num//2):
        for j in range(i):
            print(" ", end="")
        for k in range((num//2) - i):
            print("* ", end="")
        print("")

#----------------------------------------------------------#

## HOURGLASS PATTERN
def hourglass_pattern(num):
    for i in range(num//2):
        for j in range(i):
            print(" ", end="")
        for k in range((num//2) - i):
            print("* ", end="")
        print("")
    
    for i in range(1, (num//2)+1):
        for j in range((num//2) - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print("")

#----------------------------------------------------------#

## HOLLOW SQUARE PATTERN
def hollow_square_pattern(num):
    for i in range(1, num+1):
        if i in [1, num]:
            for j in range(num):
                print("* ", end="")
            print("")
        else:
            for j in range(num+1):
                if j in [0, num-1]:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print("")

#----------------------------------------------------------#

## HOLLOW FULL PYRAMID
def hollow_full_pyramid(num):
    for i in range(1, num+1):
        for j in range(num - i):
            print(" ", end="")
        for k in range(1, i+2):
            if i < num:
                if k in [1, i]:
                    print("* ", end=" ")
                else:
                    print(" ", end=" ")
            else:
                print("* ", end="")
        print("")
    
#----------------------------------------------------------#

## HOLLOW INVERTED FULL PYRAMID
def hollow_inverted_full_pyramid(num):
    for i in range(1, num+1):
        for j in range(i):
            print(" ", end="")
        for k in range((num-i)+1):
            if i != 1:    
                if k in [0, num-i]:
                    print("*", end=" ")
                else:
                    print("  ", end="")
            else:
                print("* ", end="")
        print("")

#----------------------------------------------------------#

## HOLLOW DIAMOND PYRAMID
def hollow_diamond_pyramid(num):
    for i in range(1, num+1):
        for j in range(num - i):
            print(" ", end="")
        for k in range(i+2):
            if k in [1, i]:
                print("* ", end="")
            else:
                print("  ", end="")
        print("")
    for i in range(1, num+1):
        for j in range(i):
            print(" ", end="")
        for k in range((num-i)+1):
            if k in [0, num-i]:
                print(" *", end="")
            else:
                print("  ", end="")
        print("")

#----------------------------------------------------------#

## FLOYD'S TRIANGLE
def floyd_triangle(num):
    val = 1
    for i in range(1, num+1):
        for j in range(i):
            print(f"{val} ", end="")
            val += 1
        print("")

#----------------------------------------------------------#

## PASCAL'S TRIANGLE
def pascal_triangle(num):
    for i in range(1, num+1):
        val=1
        for j in range(num - i):
            print(" ", end="")
        for k in range(1, i+1):
            if k in [1, i]:
                val = 1
            else:
                val = i-1
            print(f"{val} ", end="")
        print("")

#----------------------------------------------------------#

## K PATTERN
def k_pattern(num):
    for i in range(1,num):
        if i <= num//2:
            for j in range((num//2)+1, i, -1):
                print("* ", end="")
            print("")
        else:
            for j in range(i-(num//2-1)):
                print("* ", end="")
            print("")

#----------------------------------------------------------#

## BUTTERFLY STAR PATTERN
def butterfly_star_pattern(num):
    count = 0
    for i in range(num):
        if i <= num//2:
            for j in range(num):
                if j < count or j > num - count - 1:
                    print("* ", end="")
                else:
                    print("  ", end="")
            print("")
            count += 1     
        else:
            for j in range(num):
                if j < count or j > num - count - 1:
                    print("* ", end="")
                else:
                    print("  ", end="")
            print("")
            count -= 1


#----------------------------------------------------------#




##------------ TESTS ------------##

# right_half_pyramid(10)
# left_half_pyramid(10)
# full_pyramid(10)
# inverted_right_half_pyramid(10)
# inverted_left_half_pyramid(10)
# inverted_full_pyramid(10)
# rhombus_pattern(6)
# diamond_pattern(8)
# hourglass_pattern(8)
# hollow_square_pattern(5)
# hollow_full_pyramid(5)
# hollow_inverted_full_pyramid(6) 
# hollow_diamond_pyramid(6)
# floyd_triangle(4)
# pascal_triangle(10)
# k_pattern(8)
# butterfly_star_pattern(9)