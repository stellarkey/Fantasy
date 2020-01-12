from fantasy import *

def main():
    Sim = FantasizoneSimulator()
    Sim.create_feature()
    Sim.create_fantasizone()
    Sim.fantasizone_operation_test()

class FantasizoneSimulator():
    def create_feature(self):
        fantasy = Fantasy("I'm a fantasy.")
        another_fantasy =  Fantasy("Another fantasy.")
        reality = Reality("I'm a reality.")
        feature = Feature("I'm a feature.", [fantasy, another_fantasy, reality, Idea("New idea.", fantasy, another_fantasy)])
        feature.show_all()

    def create_fantasizone(self):
        banana = Reality("香蕉")
        strawberry = Fantasy("草莓")
        apple = Reality("苹果")
        cola = Fantasy("可乐")
        me = Fantasy("我")
        eat = Idea("爱吃", me, apple)
        drink = Idea("爱喝", me, cola)
        fruit = Feature("水果", [banana, strawberry, apple])
        love = Feature("兴趣", [eat, drink])
        love.to_fantasizone().show()
        my_knowledge = Fantasizone("我的想界", [banana, strawberry, apple, cola, fruit, me, eat])
        # my_knowledge.add(drink).add(love)
        my_knowledge.add([drink, love])
        my_knowledge.add(love)
        my_knowledge.show()
        my_knowledge.feature_reduction()
        my_knowledge.show()

    def fantasizone_operation_test(self):
        A = Reality("123")
        FZ = Fantasizone("My FZ")
        FZ.add(A).show()
        B = Fantasy("123")
        FZ.remove(B).show()
        C = Reality("312")
        D = Fantasy("321")

        M = Fantasizone("My M fantasizone")
        M.add(B).show()
        M.add([C, D]).show()
        M.clear().show()

class Fantasizone():
    """幻想空间/幻想域/想界/FZ
    A fantasizone is a collection of fantasies.
    """
    type = "fantasizone"

    def __init__(self, connotation: str = "", fantasy_list: list = []):
        self.con = connotation
        self.isEmpty = True
        self.fantasy_list = []

        if fantasy_list != []:
            self.add(fantasy_list)
            self.isEmpty = False
    
    def show(self):
        print("------------------------------")
        print("Fantasizone: \"" + self.con + "\"" + "\tTotal: " + str(len(self.fantasy_list)))
        for fantasy in self.fantasy_list:
            fantasy.simple_show()
        if self.isEmpty:
            print(" - [Empty] fantasizone.")
        return self

    def exist(self, fantasy: Fantasy):
        for fan in self.fantasy_list:
            if fan.con == fantasy.con: # when con is the same, it could be a fantasy or a reality, but not both
                return True
        return False
    
    def locate(self, fantasy: Fantasy):
        rows = len(self.fantasy_list)
        for index in range(rows):
            if self.fantasy_list[index].con == fantasy.con:
                return index
        return None # fail

    def find(self, fantasy: Fantasy):
        if self.locate(fantasy) != None:
            return self.fantasy_list[self.locate(fantasy)]
        return None

    def add(self, obj):
        if isinstance(obj, Fantasy):
            if not self.exist(obj):
                self.fantasy_list.append(obj)
                self.isEmpty = False
        if isinstance(obj, list):
            for fantasy in obj:
                self.add(fantasy)
        if isinstance(obj, Fantasizone):
            self.add(obj.fantasy_list)
        return self

    def remove(self, obj):
        if isinstance(obj, Fantasy):
            if self.exist(obj):
                self.fantasy_list.remove(self.fantasy_list[self.locate(obj)])
                if len(self.fantasy_list) == 0:
                    self.isEmpty = True
        if isinstance(obj, list):
            for fantasy in obj:
                self.remove(fantasy)
        if isinstance(obj, Fantasizone):
            if obj == self:
                self.fantasy_list.clear()
                self.isEmpty = True
            else:
                self.remove(obj.fantasy_list)
        return self

    def clear(self):
        return self.remove(self)

    def sort(self):
        """keep order: reality < fantasy < idea < feature
        """
        self.fantasy_list.sort(key=lambda x : x.sort_key)
        return self
    
    def sort_by_order(self):
        self.fantasy_list.sort(key=lambda x : x.order)
        return self

    def feature_reduction(self):
        reserve_list = []
        for fantasy in self.fantasy_list:
            if isinstance(fantasy, Feature):
                self.add(fantasy.to_fantasizone())
                reserve_list.append(fantasy)
        for feature in reserve_list:
            self.remove(feature)
        return self

    def purify(self):
        """纯化

        Purify a fantasizone so that it's fantasies are all alone(with no ideas).

        Returns:
            A purified fantasitone from the original one.
        """
        
        purity = 1.0 # purity belongs to [0, 1]; an empty fantasizone's purity is 1.0

        pass

    def is_real(self):
        pass

    def is_empty(self):
        return len(self.fantasy_list) == 0

    def realize(self):
        pass

    def reset_fantasy_orders(self):
        pass

    def get_order(self):
        """Notice: this order is the order of the whole fantasizone

        FZ_order = max{all fatasy_order}
        
        """
        order = 0.0
        for fantasy in self.fantasy_list:
            order = max(order, fantasy.order)
        return order


class Realistizone(Fantasizone):
    """现实空间/真实域/实界/RZ
    A realistizone is a collection of realities.
    """
    type = "realistizone"

    def __init__(self, connotation: str = "", reality_list: list = []):
        super(Realistizone, self).__init__(connotation, reality_list)
 

class Feature(Fantasy):
    """A basic feature inherited from Fantasy

    An idea through a feature is called as "featured idea"（特征联想）.
    A series of fetured idea with the same feature is called "featured idea group"（特征联想群）.
    A feature class contains relevant featured ideas(stored in a list).

    """
    type = "feature"
    sort_key = 4

    def __init__(self, connotation: str = "", fantasy_list: list = []):
        self.feature_idea_list = []

        super(Feature, self).__init__(connotation)

        for fantasy in fantasy_list:
            tmp_idea = Idea(fantasy.con + "-->" + self.con, fantasy, self)
            self.feature_idea_list.append(tmp_idea)
    
    def show_all(self):
        super(Feature, self).show()
        print(" - feature_ideas: ")
        for idea in self.feature_idea_list:
            idea.simple_show("\t")
        return self

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

    def to_fantasizone(self):
        FZ = Fantasizone(self.con + "[fantasizone]", [Fantasy(self.con)])
        for idea in self.feature_idea_list:
            FZ.add(idea.pre)
            FZ.add(idea)
        return FZ

       

if __name__ == '__main__':
    main()