def main():
    Sim = Simulator()
    Sim.createFantasy()
    
        
class Simulator():
    def createFantasy(self):
        print("-----------------hello, sims begin.-----------------\n")
        fantasy = Fantasy("I'm a fantasy.")
        fantasy.show()
        another_fantasy =  Fantasy("Another fantasy.")
        reality = Reality("I'm a reality.")
        reality.show()
        idea = Idea("I'm a idea.", reality, fantasy)
        idea.show()
        imbalanced_idea = Idea("I'm an imbalanced idea.", fantasy, idea)
        imbalanced_idea.show()
        feature = Feature("I'm a feature.", [fantasy, another_fantasy, reality, Idea("New idea.", fantasy, another_fantasy)])
        feature.show()

class Fantasy():
    """A basic fantasy
    """
    type = "fantasy" # type options: fantasy, reality, idea, ...
    con = "" # concept/connotation
    pre = None
    succ = None
    ''' pre&succ are "Fantasy"s being connected by this specific fantasy
    a fantasy is "None" only when it is unimaginable or it doesn't exist
    '''
    order = 0.0 # the order of it
    
    def __init__(self, connotation: str = "", pre = None, succ = None):
        self.con = connotation
        self.pre = pre
        self.succ = succ
        
        order_a = order_b = 0.0
        if pre != None:
            order_a = pre.order
        if succ != None:
            order_b = succ.order
        self.order = (order_a + order_b)/2 + 1
        
    def show(self):
        """details of a fantasy
        """
        print("con: \"" + self.con + "\"")
        print(" - type: " + self.type)
        if self.pre != None:
            print(" - pre : " + self.pre.con)
        if self.succ != None:
            print(" - succ: " + self.succ.con)
        print(" - order: " + str(self.order))

class Reality(Fantasy):
    """A basic reality inherited from fantasy
    """
    def __init__(self, connotation: str = "", pre = None, succ = None):
        super(Reality, self).__init__(connotation, pre, succ)
        self.type = "reality"
        

class Idea(Fantasy):
    """A basic idea inherited from fantasy
    """
    def __init__(self, connotation: str = "", pre = None, succ = None):
        super(Idea, self).__init__(connotation, pre, succ)
        self.type = "idea"
        
class Feature(Fantasy):
    """A basic feature inherited from Fantasy

    An idea through a feature is called as "featured idea"（特征联想）.
    A series of fetured idea with the same feature is called "featured idea group"（特征联想群）.
    A feature class contains relevant featured ideas(stored in a list).

    """
    feature_idea_list = []

    def __init__(self, connotation: str = "", fantasy_list: list = []):
        super(Feature, self).__init__(connotation)
        self.type = "feature"
        for fantasy in fantasy_list:
            tmp_idea = Idea(connotation, fantasy, self)
            self.feature_idea_list.append(tmp_idea)
    
    def show(self):
        super(Feature, self).show()
        print(" - feature_ideas: ")
        for idea in self.feature_idea_list:
            print("\t- con:\"" + idea.con + "\"", end='')
            print("\t- type: " + idea.type, end='')
            if idea.pre != None:
                print("\t- pre : " + idea.pre.con, end='')
            if idea.succ != None:
                print("\t- succ: " + idea.succ.con, end="")
            print(" - order: " + str(idea.order), end="")
            print("")

class Fantasizone():
    """幻想空间
    A fantasizone is a collection of fantasies.
    """
    empty = True
    fantasy_list = []
    def __init__(self, fantasy_list: list = []):
        if fantasy_list != []:
            self.fantasy_list = fantasy_list
    
    def show(self):
        pass

    def purify(self):
        """纯化

        Purify a fantasizone so that it's fantasies are all alone(with no ideas).

        Returns:
            A purified fantasitone from the original one.
        """
        
        purity = 1.0 # purity belongs to [0, 1]; an empty fantasizone's purity is 1.0

        pass

if __name__ == '__main__':
    main()