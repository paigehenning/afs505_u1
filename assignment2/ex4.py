print("EXERCISE 4")
print(" ")
cars=100 #number of cars available
space_in_a_car=4.0 #how many people can fit in one car excluding the driver
drivers=30 #the number of people driving
passengers=90 #the number of people who need a ride
cars_not_driven=cars-drivers #the number of cars without drivers
cars_driven=drivers #the number of cars with drivers
carpool_capacity=cars_driven*space_in_a_car #the max number of passenders today
average_passengers_per_car=passengers/cars_driven #the average number of people per car
print ("There are", cars, "cars available.")
print ("The are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

