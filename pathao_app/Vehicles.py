from abc import ABC ,abstractmethod


class Vehicle(ABC):
    speed = {
        'car' : 60,
        'bike' : 70,
        'cng' : 15
    }
    def __init__(self,vehicles_type,license_plate,rate) -> None:
        self.vehicles_type=vehicles_type
        self.license_plate=license_plate
        self.rate=rate
        self.status='available'
    
    @abstractmethod
    def start_drive(self):
         pass
         
class Car(Vehicle):
        def __init__(self, vehicles_type, license_plate, rate) -> None:
             super().__init__(vehicles_type, license_plate, rate)

        def start_drive(self):
            self.status = 'unavailable'
            print("Car started driving")

class Bike(Vehicle):
    def __init__(self, vehicles_type, license_plate, rate) -> None:
         super().__init__(vehicles_type, license_plate, rate)

    def start_drive(self):
            self.status = 'unavailable'
            print("Car started driving")
