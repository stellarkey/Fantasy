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

class Fantasy():
    """A basic fantasy
    """
    type = "fantasy" # type options: fantasy, reality, idea, ...
    sort_key = 2

    def __init__(self, connotation: str = "", pre = None, succ = None):
        self.con = connotation # concept/connotation
        self.pre = pre
        self.succ = succ
        ''' pre&succ are "Fantasy"s being connected by this specific fantasy
        a fantasy is "None" only when it is unimaginable or it doesn't exist
        '''
        
        # print(type(pre), end="; ")
        # print(type(succ))
        order_a = order_b = 0.0
        if isinstance(pre, Fantasy) and isinstance(succ, Fantasy):
            if pre != None:
                order_a = pre.order
            if succ != None:
                order_b = succ.order
            self.order = (order_a + order_b)/2 # the order of it
            if pre != None and succ != None:
                self.order += 1
        else: # str or NoneType means it's created from a recode/file
            self.order = 0
            pass # somewhere else will automatically use "set_order" function to finish it
        
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
        return self

    def simple_show(self, table: str = ""):
        print(table + " - con:\"" + self.con + "\"", end='')
        # if self.succ == None or (self.succ != None and self.succ.con != self.con):
        print("\t- type: " + self.type, end='')
        if self.pre != None:
            print("\t- pre : " + self.pre.con, end='')
        # if self.succ != None and self.succ.con != self.con:
        if self.succ != None:
            print("\t- succ: " + self.succ.con, end="")
        if self.order != 0.0:
            print("\t - order: " + str(self.order), end="")
        if self.type == "feature":
            print("\t - fantasy_list: " + str(self.get_fantasy_con_list()), end="")
        print("")
        return self

    def is_fantasy(self):
        return self.type == "fantasy"
    def is_reality(self):
        return self.type == "reality"
    def is_idea(self):
        return self.type == "Idea"
    def is_feature(self):
        return self.type == "feature"

    def set_order(self, order):
        self.order = order
        return self


class Reality(Fantasy):
    """A basic reality inherited from fantasy
    """
    type = "reality"
    sort_key = 1

    def __init__(self, connotation: str = "", pre = None, succ = None):
        super(Reality, self).__init__(connotation, pre, succ)    

class Idea(Fantasy):
    """A basic idea inherited from fantasy
    """
    type = "idea"
    sort_key = 3

    def __init__(self, connotation: str = "", pre = None, succ = None):
        super(Idea, self).__init__(connotation, pre, succ)
    
    def show_walk_through(self):
        print(self.pre.con + " --> " + self.con + " --> " + self.succ.con)
        return self
    
class RealIdea(Idea):
    type = "real_idea"
    sort_key = 3.5

    def __init__(self, connotation: str = "", pre = None, succ = None):
        super(RealIdea, self).__init__(connotation, pre, succ)


if __name__ == '__main__':
    main()