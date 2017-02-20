object_dict = {1: 'transport1', 2: 'transport2', 3: 'transport3', }
vehicle_types = ("car", "lorry", "bike")
vehicle_options = "Options are: {0}, {1}, {2}".format(vehicle_types[0], vehicle_types[1], vehicle_types[2])
loop_count = 4

class Vehicle(object):
    wheels = 4
    """define a vehicle"""
    def __init__(self, colour, model):
        self.type = "Vehicle"
        self.colour = colour
        self.model = model

class Car(Vehicle):
    """create the car class, child of Vehicle"""
    def __init__(self, colour, model):
        self.type = "Car"
        self.colour = colour
        self.model = model

class Lorry(Vehicle):
    """create the lorry class, child of Vehicle"""
    def __init__(self, colour, model):
        self.type = "Lorry"
        self.colour = colour
        self.model = model
        self.wheels = 10

class Bike(Vehicle):
    """create the bike class, child of Vehicle"""
    def __init__(self, colour, model):
        self.type = "Bike"
        self.colour = colour
        self.model = model
        self.wheels = 2

def details(veh_type, count):
    q1 = "What is the colour of the {0}? ".format(veh_type)
    q2 = "What is the model of the {0}? ".format(veh_type)
    colour = (raw_input(q1)).lower()
    model = (raw_input(q2)).lower()
    if veh_type == "car":
        object_dict[count] = Car(colour, model)
    if veh_type == "lorry":
        object_dict[count] = Lorry(colour, model)
    if veh_type == "bike":
        object_dict[count] = Bike(colour, model)
    else veh_type == "vehicle"
        object_dict[count] = Vehicle(colour, model)

def select_veh(count):
    found = False
    print vehicle_options
    while found != True:
        vehicle = raw_input("What vehicle are you inputing? ")
        if vehicle in vehicle_types:
            found = True
            details(vehicle, count)
        else:
            print "not an option"



if __name__ == "__main__":

    for i in range(1,loop_count):
        select_veh(i)
        i += 1

    for k in range(1,loop_count):
        print "-" * 15
        print "Type: " + object_dict[k].type
        print "Colour: " + object_dict[k].colour
        print "Model: " + object_dict[k].model
        print "No. of wheels: {0}".format(object_dict[k].wheels)

