from User import User
from Vehicles import Car, Bike
from datetime import datetime
from abc import ABC ,abstractmethod

class Ride_Sharing:
     
     def __init__(self,company_name) -> None:
          print('************Pathao/Uthao***************')
          self.company_name=company_name
          self.riders=[]
          self.drivers=[]
          self.rides=[]

     def add_rider(self, rider):
        self.riders.append(rider)

     def add_driver(self, driver):
        self.drivers.append(driver)
     def __repr__(self) -> str:
          return f'{self.company_name} with riders: {len(self.riders)} and drive: {len(self.drivers)}'   

class Rider(User):
     def __init__(self, name, email, NID,current_location, initial_amount) -> None:
          
          self.current_ride=None
          self.current_location=current_location
          self.initial_amount=initial_amount
          super().__init__(name, email, NID)

     def display_profile(self):
          print(f'Rider"s Name: {self.name}\n Email: {self.email}')
     def load_cash(self,amount):
          if amount>0:
               self.wallet +=amount
     def update_location(self,current_location):
          self.current_location=current_location
    # this function work id there is no ride
     def request_for_ride(self, ride_sharing, destination):
          if not self.current_ride:
               ride_request_set = Ride_request(self, destination)
               ride_matcher_set = Ride_matcher(ride_sharing.drivers)
               ride = ride_matcher_set.find_driver(ride_request_set)
               print('got the ride, allhamdulilla')
               self.current_ride = ride

     def show_current_ride(self):
          print(f"Current Ride : {self.current_ride}")

# Driver class here all details included...and current position need to call the eqcual driver
class Driver(User):
     def __init__(self, name, email, NID,current_location) -> None:
          self.current_location=current_location
          self.wallet=0
          super().__init__(name, email, NID)   

     def display_profile(self):
        print(f"Driver Name: {self.name}, Driver email: {self.email}")  

     def accept_ride(self,ride):
          ride.set_driver(self)
     # here ratings for ride
     def ride_feedback(self,feedback):
          for ride in self.ride_history:
               if ride.driver == self and ride.feedback is None:
                    ride.provide_feedback(feedback)
                    print("Thank you for your feedback!")
                    break
               else:
                    print('already provided feedback for all your rides..!!!')

# Rider class using for all details collec such as driverinfo,ride,where,when everything included
class Ride:
     def __init__(self,start_location,end_location) -> None:
          self.start_location=start_location
          self.end_location=end_location
          self.driver=None
          self.rider=None
          self.start_time=None
          self.end_time=None
          self.estimate_amount_fare=None
     def set_driver(self,driver):
          self.driver=driver
     def start_ride(self):
          self.start_time=datetime.now()

     def calculated_fare(self):
          
          return 100
     
     def end_ride(self):
          self.end_time=datetime.now()
          self.estimate_amount_fare=self.calculated_fare()
          if self.rider.wallet>=self.estimate_amount_fare:
               self.rider.wallet -=self.estimate_amount_fare
               self.driver.wallet +=self.estimate_amount_fare
               print('Ride completed!!! ')
          else:
            print("Insufficient funds in rider's wallet. Ride cannot be completed.")

          # Add ride to rider's and driver's ride history from there
          self.rider.add_ride_to_history(self)
          self.driver.add_ride_to_history(self)
     
     def __str__(self) -> str:
          return f'Ride details...\n \tStarted: {self.start_location} to {self.end_location}'
# using for ride request...where riders location include must
class Ride_request:
     def __init__(self,rider,end_location) -> None:
          self.rider=rider
          self.end_location=end_location
          
class Ride_matcher:
     def __init__(self,driver) -> None:
          self.available_driver=driver
     def find_driver(self,ride_request):
          if len(self.available_driver)>0:
               print('Find nearest driver')
               driver=self.available_driver[0]
               ride=Ride(ride_request.rider.current_location,ride_request.end_location)
               driver.accept_ride(ride)
               return ride

