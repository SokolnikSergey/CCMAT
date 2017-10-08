
from Server.Action import Action
from PyQt5.QtCore import QObject,pyqtSignal
class ActionQueue(QObject):

    action_added = pyqtSignal()
    action_is_up = pyqtSignal()

    def __init__(self):
        super(ActionQueue, self).__init__()

        self.__actions = []
    
    def add_action(self,action):
        if not self.size():
            self.action_added.emit()

        if isinstance(action,Action):
            self.__actions.append(action)

    def remove_action(self,action):
        if action is self.__actions:
            self.__actions.remove(action)

    def get_action(self):
        if (self.size()):
            return  self.__actions.pop(0)

        self.action_is_up.emit()
        return None

    def size(self):
        return len(self.__actions)


    def clear(self):
        self.__actions.clear()
        self.action_is_up.emit()