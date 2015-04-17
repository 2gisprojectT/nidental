# coding utf-8
class Lion:
    condition_ = 1  # 0 - сытый, 1 - голодный
    action_ = 0  # 0 - съесть, 1 - спать, 2 - бежать, 3 - смотреть
    __Array_ = [[[1, 1], [2, 1], [3, 1]], [[0, 0], [2, 1], [1, 1]]]

    def __init__(self, condition):
        self.condition_ = condition
        # self.action_=action

    def whoMet(self, whoMet):
        self.action_ = self.__Array_[self.condition_][whoMet][0]
        self.condition_ = self.__Array_[self.condition_][whoMet][1]

    def getCondition(self):
        return self.condition_

    def getAction(self):
        return self.action_

    # var = Lion(1,1)
    # print(var.condition_," ",var.action_)
    #
    # var.whoMet(0)
    # print(var.condition_," ",var.action_)

if __name__ == "__main__":
    condition = " "
    whoMeetLion = " "
    while condition != "exit" and whoMeetLion != "exit":
        print("Enter condition of your lion ('hungry' or 'full')")
        condition = input()
        if (condition == 'full'):
             myLion = Lion(0)
        elif(condition == 'hungry'):
             myLion = Lion(1)
        else:
            continue
        # else:
        #     print("Enter 'hungry' or 'full'!\n")
        print("Enter 'antelope','hunter' or 'tree'")
        whoMeetLion = input()
        if(whoMeetLion == "exit" or (whoMeetLion != "antelope" and whoMeetLion != "hunter" and whoMeetLion != "tree")):
            continue
        # elif(whoMeetLion != "antilope" and whoMeetLion != "hunter" and whoMeetLion != "tree"):
        #     print("Enter 'antelope','hunter' or 'tree'!")
        dictWhoMet = {"antelope": 0, "hunter": 1, "tree": 2}
        varWhoMeet = dictWhoMet.get(whoMeetLion)
        myLion.whoMet(varWhoMeet)
        currentAction = myLion.getAction()
        currentCondition = myLion.getCondition()

        dictCondition = {0: 'full', 1: 'hungry'}
        dictAction = {0: 'eat', 1: 'sleep', 2: 'run', 3: 'watch', -1: 'do nothing'}

        whatCondition = dictCondition.get(currentCondition)
        whatAction = dictAction.get(currentAction)
        print('Lion now', whatCondition, 'and', whatAction)

# if __name__ == "__main__":
#     print("Hello!\n")





