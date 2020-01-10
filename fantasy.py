def main():
    Sim = Simulator()
    Sim.createFantasy()
    
        
class Simulator():
    def createFantasy(self):
        print("-----------------hello, sims begin.-----------------\n")
        fantasy = Fantasy("Hello world! I'm a fantasy.")
        fantasy.show()
        reality = Reality("Hello world! I'm a reality.")
        reality.show()
        idea = Idea("Hello world! I'm a idea.", reality, fantasy)
        idea.show()
        imbalanced_idea = Idea("Hello world! I'm an imbalanced idea.", fantasy, idea)
        imbalanced_idea.show()

class Fantasy():
    """一个基本的幻想
    type options: fantasy, reality, idea
    """
    type = "fantasy"
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
        
    def show(self): # details of a fantasy
        print("Fantasy: \"" + self.con + "\"")
        print(" - type: " + self.type)
        if self.pre != None:
            print(" - pre : " + self.pre.con)
        if self.succ != None:
            print(" - succ: " + self.succ.con)
        print(" - order: " + str(self.order))

class Reality(Fantasy):
    """一个基本的现实
    """
    def __init__(self, connotation: str = "", pre = None, succ = None):
        super(Reality, self).__init__(connotation, pre, succ)
        self.type = "reality"
        

class Idea(Fantasy):
    """一个基本的联想
    """
    def __init__(self, connotation: str = "", pre = None, succ = None):
        super(Idea, self).__init__(connotation, pre, succ)
        self.type = "idea"
        

class Fantasizone(object):
    """幻想空间
    A fantasizone is a collection of fantasies.
    """
    def __init__(self):
        pass
    
    def purify(self):
        '''
        '''
        pass

if __name__ == '__main__':
    main()