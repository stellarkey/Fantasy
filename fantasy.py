def main():
    Sim = FantasySimulator()
    Sim.create_fantasy()
    
        
class FantasySimulator():
    def create_fantasy(self):
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
        feature.show_all()

class Fantasy():
    """A basic fantasy
    """
    type = "fantasy" # type options: fantasy, reality, idea, ...
    
    def __init__(self, connotation: str = "", pre = None, succ = None):
        self.con = connotation # concept/connotation
        self.pre = pre
        self.succ = succ
        ''' pre&succ are "Fantasy"s being connected by this specific fantasy
        a fantasy is "None" only when it is unimaginable or it doesn't exist
        '''
        
        order_a = order_b = 0.0
        if pre != None:
            order_a = pre.order
        if succ != None:
            order_b = succ.order
        self.order = (order_a + order_b)/2 # the order of it
        if pre != None and succ != None:
            self.order += 1
        
    def show(self):
        """details of a fantasy
        """
        print("con: \"" + self.con + "\"")
        print(" - type: " + self.type)
        if self.pre != None:
            print(" - pre : " + self.pre.con)
        if self.succ != None:
            print(" - succ: " + self.succ.con)
        if self.order != 0.0:
            print(" - order: " + str(self.order))

    def simple_show(self, table: str = ""):
        print(table + " - con:\"" + self.con + "\"", end='')
        if self.succ == None or (self.succ != None and self.succ.con != self.con):
            print("\t- type: " + self.type, end='')
        if self.pre != None:
            print("\t- pre : " + self.pre.con, end='')
        if self.succ != None and self.succ.con != self.con:
            print("\t- succ: " + self.succ.con, end="")
        if self.order != 0.0:
            print("\t - order: " + str(self.order), end="")
        if self.type == "feature":
            print("\t - fantasy_list: " + str(self.get_fantasy_con_list()), end="")
        print("")

    def is_fantasy(self):
        return self.type == "fantasy"
    def is_reality(self):
        return self.type == "reality"
    def is_idea(self):
        return self.type == "Idea"
    def is_feature(self):
        return self.type == "feature"


class Reality(Fantasy):
    """A basic reality inherited from fantasy
    """
    type = "reality"

    def __init__(self, connotation: str = "", pre = None, succ = None):
        super(Reality, self).__init__(connotation, pre, succ)    

class Idea(Fantasy):
    """A basic idea inherited from fantasy
    """
    type = "idea"

    def __init__(self, connotation: str = "", pre = None, succ = None):
        super(Idea, self).__init__(connotation, pre, succ)
    
    def show_walk_through(self):
        print(self.pre.con + " --> " + self.con + " --> " + self.succ.con)
        
class Feature(Fantasy):
    """A basic feature inherited from Fantasy

    An idea through a feature is called as "featured idea"（特征联想）.
    A series of fetured idea with the same feature is called "featured idea group"（特征联想群）.
    A feature class contains relevant featured ideas(stored in a list).

    """
    type = "feature"

    def __init__(self, connotation: str = "", fantasy_list: list = []):
        self.feature_idea_list = []

        super(Feature, self).__init__(connotation)

        for fantasy in fantasy_list:
            tmp_idea = Idea(connotation, fantasy, self)
            self.feature_idea_list.append(tmp_idea)
    
    def show_all(self):
        super(Feature, self).show()
        print(" - feature_ideas: ")
        for idea in self.feature_idea_list:
            idea.simple_show("\t")

    def get_fantasy_list(self):
        fantasy_list = []
        for idea in self.feature_idea_list:
            fantasy_list.append(idea.pre)
        return fantasy_list
    def get_fantasy_con_list(self):
        fantasy_name_list = []
        fantasy_list = self.get_fantasy_list()
        for fantasy in fantasy_list:
            fantasy_name_list.append(fantasy.con)
        return fantasy_name_list
            

class Fantasizone():
    """幻想空间
    A fantasizone is a collection of fantasies.
    """
    
    def __init__(self, connotation: str = "", fantasy_list: list = []):
        self.con = connotation
        self.isEmpty = True
        self.fantasy_list = []

        if fantasy_list != []:
            self.fantasy_list = fantasy_list
            self.isEmpty = False
    
    def show(self):
        print("Fantasizone: " + self.con)
        for fantasy in self.fantasy_list:
            fantasy.simple_show()

    def exist(self, fantasy: Fantasy):
        for fan in self.fantasy_list:
            if fan == fantasy:
                return True
        return False
    
    def add(self, fantasy: Fantasy):
        if not self.exist(fantasy):
            self.fantasy_list.append(fantasy)
            isEmpty = False
            return True # succeed
        return False # fail to add

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