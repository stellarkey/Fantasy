from fantasy import *

def main():
    Sim = FantasyAlgorithmsSimulator()
    Sim.isolation_test()
    
        
class FantasyAlgorithmsSimulator():
    def isolation_test(self):
        banana = Reality("香蕉")
        # banana.show()
        strawberry = Fantasy("草莓")
        # strawberry.show()
        apple = Reality("苹果")
        # apple.show()
        cola = Fantasy("可乐")
        # cola.show()
        me = Fantasy("我")
        # me.show()
        eat = Idea("爱吃", me, apple)
        # eat.show_walk_through()
        drink = Idea("爱喝", me, cola)
        # drink.show_walk_through()
        fruit = Feature("水果", [banana, strawberry, apple])
        # fruit.show_all()
        love = Feature("爱好/兴趣", [eat, drink])
        love.show_all()
        
        my_knowledge = Fantasizone("我的知识领域", [banana, strawberry, apple, cola, fruit, me, eat])
        my_knowledge.show()
        print("------------------------")
        print("可乐是孤立的吗？ ", is_isolated(cola, my_knowledge))
        print("苹果是孤立的吗？ ", is_isolated(apple, my_knowledge))
        print("------------------------")
        my_knowledge.add(drink)
        my_knowledge.show()
        print("可乐是孤立的吗？ ", is_isolated(cola, my_knowledge))
        print("------------------------")
        my_knowledge.add(love)
        # my_knowledge.show()



def is_isolated(fantasy: Fantasy, fantasizone: Fantasizone):
    """Judging whether a fantasy is isolated in the fantasizone or not
    """
    for fan in fantasizone.fantasy_list:
        if fan.pre == fantasy or fan.succ == fantasy:
            return False
    return True


if __name__ == '__main__':
    main()