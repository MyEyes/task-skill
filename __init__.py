import imp
import os
import traceback
import logging
import re

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.audio import wait_while_speaking 
from mycroft.util.log import getLogger
from lingua_franca.format import pronounce_number
from .storage import DatabaseStorage

logger = getLogger(__name__)

__author__ = "MyEyes"

class taskSkill(MycroftSkill):
    def __init__(self) -> None:
        super(taskSkill, self).__init__(name="taskSkill")
        try:
            self.__initStorage()
        except Exception as e:
            self.speak_dialog("init_storage_err")
            self.storage = None

    def __initStorage(self):
        if self.settings.get('store_mode') == "database":
            self.storage = DatabaseStorage(self.settings.get('database_addr'),self.settings.get('database_name'),self.settings.get('database_user'),self.settings.get('database_pass'),)

    def stop(self):
        pass

    def ask_user_confirm(self, phrase, args=None):
        response = self.get_response(phrase, args)
        yes_words = set(self.translate_list('yes')) # get list of confirmation words
        resp_split = response.split() 
        if any(word in resp_split for word in yes_words): # if user said yes
            return True
        return False

def create_skill():
    return taskSkill()
