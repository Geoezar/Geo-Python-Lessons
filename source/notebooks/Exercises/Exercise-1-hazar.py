#Question 1:
ice_cream_rating = 7
sleeping_rating = 6
print("I love eating ice cream " + str(ice_cream_rating) + " out of 10")
print("I love sleeping " + str(sleeping_rating) + " out of 10")

#Question 2:
first_name = "Hazar"
last_name = "Kuru"
my_name = first_name + " " + last_name
print(my_name)

#Question 3:
happiness_rating = (ice_cream_rating + sleeping_rating) / 2
print(happiness_rating)

#Question 4:
print(type(ice_cream_rating))
print(type(first_name))
print(type(happiness_rating))

#Question 5:
print("My name is " + first_name + " " + last_name + " and I give eating ice cream a score of " + str(ice_cream_rating) + " out of 10!")
print("I am " + first_name + " " + last_name + " and my sleeping enjoyment rating is " + str(sleeping_rating) + " / 10!")
print("Based on the factors above, my happiness rating is " + str(happiness_rating) + " out of 10, or " + str(happiness_rating * 10) + " %")