#defining variables set to specific values.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#variables derived from previous set values
cars_not_driven = cars - drivers #each car can only have 1 driver
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car #how many total seats are available in all cars
avg_passengers_per_car = passengers / cars_driven

#printing out info with the variables defined above
print "There are", cars, "available"
print "There are only", drivers, "available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", avg_passengers_per_car, "in each car"