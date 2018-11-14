##functions for handling PyObjHandles - Spellslinger
from toee import *

def getIDfromObjHandle(objhandle):
    string = str(objhandle)
    #get ID number
    ID = string.split("(")[1][:-1]
    return long(ID)


def getObjHandleFromID(ID):
    return PyObjHandle(ID)
    

def derefHandle(objhandle):
    """Return serialized data of the PyObjHandle."""
    return objhandle.__getstate__()
    

def refHandle(serialdata):
    """Reconstruct PyObjHandle from serialized data."""
    objhandle = PyObjHandle()
    objhandle.__setstate__(serialdata)
    return objhandle
