##DLL calls these functions to enable the persistent data scheme - Spellslinger
import _include
from co8Util.Logger import Logger
from co8Util.PersistentData import Co8PersistentData

def save(savename):
##    logger = Logger(__name__)
##    logger.logme("save:" + savename)
    Co8PersistentData.save(savename)

def load(savename):
##    logger = Logger(__name__)
##    logger.logme("load:" + savename)
    Co8PersistentData.load(savename)

def init():
    pass
