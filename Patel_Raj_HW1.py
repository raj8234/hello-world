#Author: Raj Patel
#Homework Number & Name: #1 Electric Scooter Sharing – usage
#Due Date: 9-16-18
#Program Description: Calculate bill, average travel time, and battery percentage after trip when using a scooter given information from the user.

#User asked for starting location
origin = input("What location are you going to start at? ")
#User asked for ending destination
destination = input("Where are you trying to go? ")
#User asked for distanced traveled in miles
distance_traveled = float(input("How many miles is this trip? "))
#User asked for average speed during trip in miles per hour
average_speed = float(input("What is your average speed during the trip in miles per hour? "))
#User asked for percentage of battery remaining on scooter before trip as a whole number
battery_remaining_before_trip = float(input("What is the battery percentage remaining on your scooter? "))

#calculate time to complete trip in minutes
#1.convert miles per hours into miles per minute
average_speed_mpm = average_speed/60
#2.calculate time in minutes for entire trip
time_to_complete_trip = (distance_traveled/average_speed_mpm)
#calculate cost of trip with initial start cost and charge per minute and without tax
cost_of_trip_no_tax = 1.00 + (.15*time_to_complete_trip)
#calculate tax cost of the trip with a 7.25% tax
tax_of_trip = cost_of_trip_no_tax*.0725
#calculate total cost of trip with tax
total_cost_of_trip = cost_of_trip_no_tax + tax_of_trip
#calculate battery percentage remaining after trip
battery_remaining_after_trip = battery_remaining_before_trip - (distance_traveled*5)
#convert battery percentage remaining after trip into decimal format
battery_remaining_after_trip = (battery_remaining_after_trip/100)

#blank line for organization
print('')

#output trip information (start location to end location)
print("Trip:", origin, 'to', destination)
#output distance of trip in miles
print("Proposed distance (miles):", format(distance_traveled, '.1f'))
#output average speed in miles per hour
print("Average speed (miles per hour):", format(average_speed, '.1f'))
#output time to complete trip in minutes
print("Time to complete trip (minutes):", format(time_to_complete_trip, '.1f'))
#output cost of trip without tax
print("Cost of trip: $", format(cost_of_trip_no_tax, '.2f'), sep='')
#output tax cost of trip
print("Taxes incurred: $", format(tax_of_trip, '.2f'), sep='')
#output total cost of trip with tax
print("Total trip cost: $", format(total_cost_of_trip, '.2f'), sep='')
#output battery percentage remaining after trip in percent format
print("Percent scooter battery remaining after trip is completed:", format(battery_remaining_after_trip,'.2%'))

                     
                           
