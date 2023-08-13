class Vehicle:
    name = "car1"
    nature = "Fer"
    type = "convertible"
    color = "red" 
    price = 60000.00

    def car_description(self):
     descript = "%s is %s. Its name is %s and it is a %s worth $%.2f " % (self.name,self.color,self.nature,self.type,self.price)
     return descript

car1 = Vehicle()

car2 = Vehicle()
car2.name = "car2"
car2.nature = "Jump"
car2.type = "van"
car2.color = "blue"
car2.price = 10000.00

print(car1.car_description())
print(car2.car_description())




