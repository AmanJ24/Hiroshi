class game:
    def __init__(self, User_ID, Username):
        self.id = User_ID
        self.name = Username
        self.health = 100
        self.power = 50

    def attack(self, user):
        user.health -= 10
        self.power += 10    


user_1 = game("001", "Manveer")
user_2 = game("002", "Aman")

user_2.attack(user_1)

print(user_2.health)
print(user_2.power)
print(user_1.health)
print(user_1.power)
