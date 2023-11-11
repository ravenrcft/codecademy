class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

sloth = Animal("Slowbert", 2)
ocelot = Animal("Checker", 1)
hippo = Animal("Bobert",3)
hippo.description()

print sloth.health
print ocelot.health
print hippo.health