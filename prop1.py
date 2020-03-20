class Vehicle:
   def __init__(self):
     self.seat = None
     self.wheel = None
     self.door = None
   def set_seat(self, seat):
      self.seat = seat
   def set_wheel(self, wheel):
      self.wheel = wheel
   def set_door(self, door):
       self.door = door
   def serve(self):
       print("Seat: " + self.seat + ", Wheel: " + self.wheel + ",Door: "+self.door)


class VehicleBuilder:
   def __init__(self):
        self.vehicle = None

   def get_vehicle(self):
       return self.vehicle

   def create_new_vehicle_product(self):
       self.vehicle = Vehicle()

class CarBuilder(VehicleBuilder):
       def build_seat(self):
           self.vehicle.set_seat("CarSeat")

       def build_door(self):
            self.vehicle.set_door("CarDoor")

       def build_wheel(self):
           self.vehicle.set_wheel("CarWheel")

class BikeBuilder(VehicleBuilder):
       def build_seat(self):
           self.vehicle.set_seat("BikeSeat")

       def build_door(self):
            self.vehicle.set_door("")

       def build_wheel(self):
           self.vehicle.set_wheel("BikeWheel")

class TruckBuilder(VehicleBuilder):
       def build_seat(self):
           self.vehicle.set_seat("TruckSeat")

       def build_door(self):
            self.vehicle.set_door("TruckDoor")

       def build_wheel(self):
           self.vehicle.set_wheel("TruckWheel")

class Manufacturer:
       def __init__(self):
           self.VehicleBuilder = None

       def set_vehicle_builder(self, pb):
           self.VehicleBuilder = pb

       def get_vehicle(self):
           return self.VehicleBuilder.get_vehicle()

       def construct_vehicle(self):
           self.VehicleBuilder.create_new_vehicle_product()
           self.VehicleBuilder.build_door()
           self.VehicleBuilder.build_wheel()
           self.VehicleBuilder.build_seat()


if __name__ == '__main__':
   manufacturer = Manufacturer()
   manufacturer.set_vehicle_builder(BikeBuilder())
   manufacturer.construct_vehicle()
   vehicle = manufacturer.get_vehicle()
   vehicle.serve()

   manufacturer.set_vehicle_builder(CarBuilder())
   manufacturer.construct_vehicle()
   vehicle = manufacturer.get_vehicle()
   vehicle.serve()

   manufacturer.set_vehicle_builder(TruckBuilder())
   manufacturer.construct_vehicle()
   vehicle = manufacturer.get_vehicle()
   vehicle.serve()

