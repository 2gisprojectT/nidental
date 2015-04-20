# coding utf-8
class Lion:

    def __init__(self,table, condition):
        self.condition_ = condition
        if(table=={}):
            raise Exception('Empty table!!!')
        self.table_ = table
        self.action_ = -1

    def getCondition(self):
        return self.condition_

    def whoMet(self, whoMet):
        # if (not(whoMet in self.table_)):#проверка на наличи в таблице соотв
        #     return False
        self.action_ = self.table_[self.condition_][whoMet][0]
        self.condition_ = self.table_[self.condition_][whoMet][1]

    def getAction(self):
        return self.action_

    def getTable(self):
        return self.table_


if __name__ == "__main__":
    condition = " "
    whoMeetLion = " "
    table = [[[1, 1], [2, 1], [3, 1]], [[0, 0], [2, 1], [1, 1]]]
    # 0 - съесть, 1 - спать, 2 - бежать, 3 - смотреть
    # 0 - сытый, 1 - голодный
    dictWhoMet = {"antelope": 0, "hunter": 1, "tree": 2}
    dictCondition = {0: 'full', 1: 'hungry'}
    dictAction = {0: 'eat', 1: 'sleep', 2: 'run', 3: 'watch', -1: 'do nothing'}

    print("Enter condition of your lion 'hungry' or 'full'('exit' to exit programm)")
    condition = input()
    if (condition == 'full'):
        conditionIndex=0
    elif(condition == 'hungry'):
        conditionIndex=1
    myLion = Lion(table,conditionIndex)

    while condition != "exit" and whoMeetLion != "exit":
        print("Enter 'antelope','hunter' or 'tree'('exit' to exit programm)")
        whoMeetLion = input()
        if(whoMeetLion == "exit" or (whoMeetLion != "antelope" and whoMeetLion != "hunter" and whoMeetLion != "tree")):
            print("Enter only 'antelope','hunter' or 'tree'('exit' to exit programm)!")
            continue
        varWhoMeet = dictWhoMet.get(whoMeetLion)
        myLion.whoMet(varWhoMeet)
        currentAction = myLion.getAction()
        currentCondition = myLion.getCondition()
        whatCondition = dictCondition.get(currentCondition)
        whatAction = dictAction.get(currentAction)
        print('Lion now', whatCondition, 'and', whatAction)





