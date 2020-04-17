class Arrangement:

    def __init__(self):
        self.__flowers = []

    def enhance(self, flower):
        if flower.supply >=10:
             self.__flowers.append(flower)
             print(f"The {flower.name} were added to the arrangement!")
             flower.supply-= 10

        else:
            print(f"I am sorry but the {flower.name} are in short supply and we don't have enough to add this to the current arrangement")
    
    @property
    def flowers(self):
        return self.__flowers
    
    @flowers.setter
    def flowers(self, flower):
            self.__flowers.append(flower)



class MothersDay(Arrangement):

    def __init__(self): 
        super().__init__()
    # Override the `enhance` method to ensure that
    # roses, lillies, and alstroemeria can't be added

    def enhance(self, flower):
        
        if flower.supply >=10:
            if flower.name == "Daisies" or "Baby's Breath" or "Poppies":
                self.flowers=flower
                print(f"The {flower.name} were added to the arrangement!")
                flower.supply-= 10
            else:
                print(f"I am sorry, but {flower.name} aren't allowed in the Mother's Day arrangement.")
        else:
            print(f"I am sorry but the {flower.name} are in short supply and we don't have enough to add this to the current arrangement")
     


class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        if flower.supply >=10:
            if flower.name == "Roses" or "Lilies" or "Alstroemerias":
                self.flowers = flower
                print(f"The {flower.name} were added to the arrangement!")
                flower.supply-= 10
            else:
                print(f"I am sorry, but {flower.name} aren't allowed in the Mother's Day arrangement.")
        else:
            print(f"I am sorry but the {flower.name} are in short supply and we don't have enough to add this to the current arrangement")
    

    
class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.supply = 100

    
class IOrganic:
    def __init__(self):
        self.organic = True
        self.stem_length = "4in"
    
    def transport_flowers(self, name):
        print(f"The {name} were transported in a non-refrigerated case")
    

class INotOrganic:
    def __init__(self):
        self.organic =False
        self.stem_length = "7in"

    def transport_flowers(self, name):
        print(f"The {name} were transported in a refrigerated case")



class Rose(Flower, INotOrganic):
    def __init__(self, color):
        Flower.__init__(self, 'Roses', color)
        INotOrganic.__init__(self)

class Daisy(Flower, IOrganic):
    def __init__(self, color ):
        Flower.__init__(self,"Daisies",  color)
        IOrganic.__init__(self)



class Babys_Breath(Flower, IOrganic):
    def __init__(self, color ):
        Flower.__init__(self,"Baby's Breath",  color)
        IOrganic.__init__(self)


class Poppy(Flower, IOrganic):
    def __init__(self, color):
        Flower.__init__(self, "Poppies", color)
        IOrganic.__init__(self)


class Lily(Flower, INotOrganic):
    def __init__(self, color):
        Flower.__init__(self,'Lilies', color)
        INotOrganic.__init__(self)

class Alstroemeria(Flower, INotOrganic):
    def __init__(self, color):
        Flower.__init__(self, "Alstroemerias", color)
        INotOrganic.__init__(self)



    
    



if __name__ == "__main__":

    for_beth = ValentinesDay()
    red_roses = Rose("Red")
    
    daisies = Daisy("Yellow")
    poppies = Poppy("Red")
    babies = Babys_Breath('White')
    lilies = Lily("Pink")
    alstroemerias = Alstroemeria("Yellow")

    for_mom = MothersDay()
    # print(red_roses.name, daisies.name, poppies.stem_length, lilies.color, alstroemerias.organic)
    # babies.transport_flowers(babies.name)
    # lilies.transport_flowers(lilies.name)
   
   
    for_beth.enhance(red_roses)
    for_beth.enhance(lilies)
    for_beth.enhance(alstroemerias)
    for_mom.enhance(daisies)
    for_mom.enhance(poppies)
    for_mom.enhance(babies)
    for_mom.enhance(red_roses)

    # print (red_roses.supply)
