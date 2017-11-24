"""MARIA DE LOS ANGELES RIOYOS HERRERA
************GITI9072-e*****************
####UNIDAD 3: PATRONES DE DISEÑO######"""


class House(object): #The class being visited
    def accept(self, visitor):
        """INTERFACE TO ACCEPT A VISITOR"""
        #Triggers the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by",hvac_specialist) #Note that now have a reference to the HVAC specialist in the house object!
 
    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)#Note that we now have  a reference to the electrician  object in the house object!

    def __str__(self):
         """Simply return the class name when the House object is printed"""
         return self.__class__.__name__

class Visitor(object):
   """Abstract visitor"""
def __str__(self):
        """simply return the class name when the Visitor object is printed"""
        return self.__class__.__name__

class HvacSpecialist(Visitor): #INHERITS FROM THE PARENT CLASS, VISITOR
    """Concrete  vivitor: HVAC apecialist"""
    def visit(self, house):
        house.work_on_hvac(self) #Note that the visitor now has a reference to the house object

class Electrician(Visitor): #Inherits from the parent clas, Visitor
    """Concrete visitor:electrician"""
    def visit(self, house):
        house.work_on_electricity(self)#Note that the visitor now has a reference to the house object
        
#Create ab HVAC specialist
hv = HvacSpecialist()
#Create an electrician
e = Electrician()

#Create = House
home = House()

#Let the house accept the HVAC specialist and work  on the house by invoring  the visit() method
home.accept(hv)

#Let the house accept the electrician and work  on the house by invoring  the visit() method
home.accept(e)




