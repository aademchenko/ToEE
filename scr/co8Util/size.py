##functions for handling size mods - Spellslinger
from toee import *

def decSizeCategory(objhandle):
##    #set new size - not a good idea, gives you 2x the penalty
    sizeCat = objhandle.obj_get_int(obj_f_size)
    sizeCat -= 1
##    objhandle.obj_set_int(obj_f_size, sizeCat)
    #set new reach
    objhandle.obj_set_int(obj_f_critter_reach, getReachForSizeCategory(sizeCat))


def incSizeCategory(objhandle):
##    #set new size - not a good idea, gives you 2x the penalty
    sizeCat = objhandle.obj_get_int(obj_f_size)
    sizeCat += 1
##    objhandle.obj_set_int(obj_f_size, sizeCat)
    #set new reach
    objhandle.obj_set_int(obj_f_critter_reach, getReachForSizeCategory(sizeCat))


def resetSizeCategory(objhandle):
##    #set new size - not a good idea, gives you 2x the penalty
    sizeCat = objhandle.obj_get_int(obj_f_size)
##    objhandle.obj_set_int(obj_f_size, sizeCat)
    #set new reach
    objhandle.obj_set_int(obj_f_critter_reach, getReachForSizeCategory(sizeCat))


def getReachForSizeCategory(sizeCat):
    #just differentiating medium and large for now
    if sizeCat <= STAT_SIZE_MEDIUM:
        return 0
    else:
        return 10
