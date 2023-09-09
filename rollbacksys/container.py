import os

from rollbacksys.maintainer import Action
from rollbacksys.maintainer import ActionPass


class ActionCon:
    __actions: dict = {}
    __action_passes: list = []
    __max_action_pass: int

    def __init__(self, max_action_pass: int):
        self.__max_action_pass = max_action_pass

    def add_action(self, action: Action):
        self.__actions.update({action.name: action})

    def add_action_pass(self, action_path: ActionPass):
        self.__action_passes.append(action_path)

        while len(self.__action_passes) > self.__max_action_pass:
            self.__action_passes.pop(0)

    def clear(self):
        self.__action_passes.clear()

    def rollback(self):
        length = len(self.__action_passes)

        self.__actions[self.__action_passes[length - 1].name] \
            (*self.__action_passes[length - 1].parameters)



