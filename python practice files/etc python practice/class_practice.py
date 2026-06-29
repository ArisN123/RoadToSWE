

# class restaurant():

#     def __init__(self,res_name,cuis_type):
#         self.restaurant_name = res_name
#         self.cuisine_type = cuis_type

#     def describe_restaurant(self):
#         print(f'the restaurants name is {self.restaurant_name} the cuisine type is {self.cuisine_type}')
        
#     def open_restaurant(self):
#         print(f'the restaurant {self.restaurant_name} is now open')



# gamer = restaurant('GamerWorld','Chinese')

# gamer.describe_restaurant()

# gamer.open_restaurant()


class User():
    def __init__(self,first,last,age,height,weight):
        self.first_name = first
        self.last_name = last
        self.age = age 
        self.height = height
        self.weight = weight
        self.gamer = 0
    
    def describe_user(self):
        print(f'\t first name is {self.first_name.title()},\n\t last name is {self.last_name.title()},\n\t age is {str(self.age)},\n\t height is {str(self.height)},\n\t weight is {str(self.weight)}')

    def greet_user(self):
        print(f'hello {self.first_name.title()} {self.last_name.title()}')


user1 = User('aris','niamonitakis',24,183,78)

user1.greet_user()

print(user1.gamer)

user1.gamer = user1.gamer + 50

print(user1.gamer)


