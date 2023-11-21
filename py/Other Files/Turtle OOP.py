# # from turtle import Turtle, Screen 

# # timmy = Turtle()
# # print(timmy)
# # timmy.shape("turtle")
# # timmy.color("coral")
# # timmy.forward(100)
# # timmy.right(90)
# # timmy.forward(100)

# # my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# table.align = "l"
# table.header_style = "title"
# print(table)



# print(ord('a') - 96)
# print(ord('A') - 64)

# print(chr(11 + 96))
# print(chr(11 + 64))

text = input()

def encrypt(t):
    chars = list(text)
    allowed_characters = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.?!")

    for char in chars:
        for i in allowed_characters:
            if char == i:
                chars[chars.index(char)] = allowed_characters.index(i)
    return chars

print(encrypt(text))