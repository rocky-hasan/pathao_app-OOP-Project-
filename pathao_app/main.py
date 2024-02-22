from pathao import Ride_Sharing,Rider,Driver
from Vehicles import Car,Bike


# Add company name 
Pick__Up = Ride_Sharing('Pick Up')
# make riders details  (self, name, email, NID,current_location, initial_amount) 
Rakib = Rider('Md Rakibul Hasan', 'Rakib@gmail.bd', 1234, 'Bashundhara', 1200)
# ad rider and collect data 
Pick__Up.add_rider(Rakib)
Driver_Moshtak = Driver('Moshtak', 'Moshtak@gmail.com', 5643, 'Gulshan-2')
Pick__Up.add_driver(Driver_Moshtak)
print(Pick__Up)
Rakib.request_for_ride( Pick__Up, 'Uttara Gramer Bari')
Rakib.show_current_ride()
# this portion i test vehicles
car = Car('car', 'ABC123', 20)
bike = Bike('bike', 'XYZ456', 10)

# Output: available
print(car.status)  
car.start_drive()
# Output: unavailable
print(car.status)  

 # Output: available
print(bike.status) 
bike.start_drive()
 # Output: unavailable
print(bike.status) 