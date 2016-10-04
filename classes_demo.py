vehicle_types = ("car", "lorry", "bike")
vehicle_options = "Options are: {0}, {1}, {2}".format(vehicle_types[0], vehicle_types[1], vehicle_types[2])

class Vehicle(object):
    """define a vehicle"""
    def __init__(self, colour, model):
        self.colour = colour
        self.colour = model
        wheels = 4

class Car(Vehicle):
    """create the car class, child of Vehicle"""
    def __init__(self, colour, model):
        self.colour = colour
        self.colour = model


def details(veh_type, count):
    q1 = "What is the colour of the {0}? ".format(veh_type)
    q2 = "What is the model of the {0}? ".format(veh_type)
    colour = raw_input(q1)
    model = raw_input(q2)
    print colour
    print model
    print count
#    if veh_type == "Car":




def select_veh(count):
    found = False
    print "hello"
    print vehicle_options
    while found != True:
        vehicle = raw_input("What vehicle are you inputing? ")
        if vehicle in vehicle_types:
            found = True
            details(vehicle, count)
        else:
            print "not an option"



if __name__ == "__main__":

    i = 3
    while i > 0:
        select_veh(i)
        i -=1
        print i