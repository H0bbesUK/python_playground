class Parent(object):
    """docstring for Parent"""
    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT override()"

    def altered(self):
        print "PARENT altered()"

    def random(self):
        x = 1
        while x < 20:
            print "WIBBLE, MARCOS, FISH HEADS"
            x += 1

class Child(Parent):
    """docstring for Child"""
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

class Teen(Parent):
    def override(self):
        #print "I'm a TEENAGER FFS"
        super(Teen, self).random()



dad = Parent()
son = Child()
jason = Teen()

dad.implicit()
son.implicit()     

dad.override()
son.override()

dad.altered()
son.altered()

print "--------TEEN---------"
jason.implicit()
jason.override()
jason.altered()