from abc import ABC ,abstractmethod
class User(ABC):
     def __init__(self, name, email, NID) -> None:
        self.name = name
        self.email = email
        self.__id = 0
        self.__NID = NID
        self.wallet = 0
        self.ride_history = []
    # adding riding history or data
     def add_ride_history(self,ride):
         if isinstance(ride,Ride):
            self.ride_history.append(ride)
         else:
             print("Invalid Ride Data")
      # get all data from self.ride_history = [] 
     def get_ride_history(self):
         return self.ride_history
        
     def display_profile(self):
          raise NotImplementedError 
     