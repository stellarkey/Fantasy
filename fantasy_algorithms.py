from necessary import * # 引入引库程序
from fantasy import *
from fantasizone import *

def main():
    Sim = FantasyAlgorithmsSimulator()
    Sim.isolation_test()
    Sim.create_fantasizone_from_csv()
    
        
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
        # love.show_all()
        
        my_knowledge = Fantasizone("我的知识领域", [banana, strawberry, apple, cola, fruit, me, eat])
        my_knowledge.show()
        print("------------------------")
        print("可乐是孤立的吗？ ", is_isolated(cola, my_knowledge))
        print("苹果是孤立的吗？ ", is_isolated(apple, my_knowledge))
        print("------------------------")
        my_knowledge.add(drink)
        my_knowledge.show()
        print("------------------------")
        print("可乐是孤立的吗？ ", is_isolated(cola, my_knowledge))
        print("------------------------")
        my_knowledge.remove(drink)
        my_knowledge.show()
        print("------------------------")
        print("可乐是孤立的吗？ ", is_isolated(cola, my_knowledge))
        print("------------------------")
        # my_knowledge.add(love)
        # my_knowledge.show()

    def create_fantasizone_from_csv(self):
        filepath = "data/fantasizone_example.csv"
        print(pd.read_csv(filepath))
        fz = csv_to_fantasizone(filepath, "测试想界")
        fz.show()
        fz.feature_reduction()
        fz.show()
        fz.sort().show()
        fz.sort_by_order().show()
        print("===> FZ's order =", fz.get_order())


def is_isolated(fantasy: Fantasy, fantasizone: Fantasizone):
    """Judging whether a fantasy is isolated in the fantasizone or not
    """
    for fan in fantasizone.fantasy_list:
        if fan.pre == fantasy or fan.succ == fantasy:
            return False
    return True

def df_sort(df: pd.DataFrame):
    """keep order: reality < fantasy < idea < feature
    """
    # print(df['type'])
    df['marker'] =df.apply(lambda x: 1 if x.type=="reality" else (2 if x.type=="fantasy" else (3 if x.type=="idea" else 4)) , axis=1)
    df = df.sort_values(by=['marker'])
    df = df.reset_index(drop = True)
    return df

def df_to_fantasizone(df: pd.DataFrame, Name: str):
    df = df_sort(df)
    FZ = Fantasizone(Name) # empty initialzation
    rows = df.shape[0]
    for i in range(rows):
        if df['type'][i] == "fantasy":
            FZ.add(Fantasy(df['con'][i]))
        elif df['type'][i] == "reality":
            FZ.add(Reality(df['con'][i]))
        elif df['type'][i] == "idea":
            f1, f2 = Fantasy(df['pre'][i]), Fantasy(df['succ'][i])
            if FZ.exist(f1):
                PRE = FZ.find(f1)
            else:
                FZ.add(f1) # f1 might exists then no actions
                PRE = f1
            if FZ.exist(f2):
                SUCC = FZ.find(f2)
            else:
                FZ.add(f2) # f2 might exists then no actions
                SUCC = f2
            FZ.add(Idea(df['con'][i], PRE, SUCC).set_order(float(df['order'][i])))
            # Note: the order from date might be wrong, so it shall be checked after
        elif df['type'][i] == "feature":
            tmp_list = df['fantasy_list'][i].split(",")
            tmp_fantasy_list = []
            for tmp in tmp_list:
                tmp_fantasy = Fantasy(tmp)
                if FZ.exist(tmp_fantasy):
                    tmp_fantasy_list.append(FZ.find(tmp_fantasy))
                else:
                    tmp_fantasy_list.append(tmp_fantasy)
            FZ.add(Feature(df['con'][i], tmp_fantasy_list))
    return FZ

def csv_to_fantasizone(filepath: str, Rename: str = ""):
    df = pd.read_csv(filepath, encoding=chardet.detect(open(filepath,'rb').read())['encoding'])
    # print(isinstance(df, pd.DataFrame))
    if Rename:
        return df_to_fantasizone(df, Rename)
    else:
        return df_to_fantasizone(df, filepath.split("/")[-1])

def fantasizone_to_csv(fantasizone: Fantasizone, filepath: str):
    pass

if __name__ == '__main__':
    main()