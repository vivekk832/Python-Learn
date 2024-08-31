class Car:
    totalCar = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.totalCar +=1

    def chai_brand(self):
        return self.__brand + " !"

# __ means object is private now , class can access it but none of the created object can access it.

    def full_name(self ):
        return f"{self.__brand} {self.__model}"


    def fuel_type(self):
        return "Petrol or Diesal"
    

    @staticmethod
    def general_description():
        return "Cars are amazing!"
    
    @property
    def model(self):
        return self.__model
    


    
    
    
# Interitance 
class ElectricCar(Car):
    def __init__(self, brand , model, battery_size):
        # self.brand = brand // no need to do this 
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

# my_tesla = ElectricCar("Tesla", "Models S","85kWh")

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))


# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car= Car("Tata","safari")
# my_car.model = "City"

# Car("Tata","Nexon")

# print(my_car.model)
# safari3 = Car("Tata","nexon")
# print(safari.fuel_type())
# print(my_car.general_description())
# print(Car.general_description())

# print(Car.totalCar)

# read about setter





        
        



# my_car = Car("Toyota","Corolla")
# print(my_car.brand,my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.model)



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is Engine "

class ElectricCarTwo(Battery,Engine , Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla)
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())