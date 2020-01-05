def main():
    test = Fantasy("Hello world!")
    test.show()
    pass

class Fantasy(object):
    """一个基本的幻想
    type options: fantasy, reality, idea

    """
    type = ""
    con = "" # connotation
    pre = None
    succ = None
    order = 0.0

    def __init__(self, connotation: str = "", pre: Fantasy = None, succ: Fantasy = None):
        self.type = "fantasy"
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
        print("Fantasy: \"" + self.con + "\"")
        print(" - type: " + self.type)
        if self.pre != None:
            print(" - pre : " + self.pre.con)
        else:
            print(" - pre : " + "None")
        if self.succ != None:
            print(" - succ: " + self.succ.con)
        else:
            print(" - succ: " + "None")
        print(" - order: " + str(self.order))

class Reality(object):
    pass

class Idea(object):
    pass

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