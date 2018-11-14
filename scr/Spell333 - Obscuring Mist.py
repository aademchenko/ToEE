from toee import *
import _include
from co8Util import size
from co8Util.PersistentData import *
from co8Util.ObjHandling import *

OBSCURING_MIST_KEY = "Sp333_Obscuring_Mist_Activelist"



def OnBeginSpellCast( spell ):
	print "Obscuring Mist OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Obscuring Mist OnSpellEffect"

	
	spell.duration = 100 * spell.caster_level
	
	if spell.caster.name == 8002 and game.leader.map == 5005: # Lareth in Moathouse
		locc_ = 483L + (534L << 32)
	else:
		locc_ = spell.target_loc

	# spawn one spell_object object
	spell_obj = game.obj_create( OBJECT_SPELL_GENERIC, locc_ )


	# add to d20initiative
	caster_init_value = spell.caster.get_initiative()
	spell_obj.d20_status_init()
	spell_obj.set_initiative( caster_init_value )

	# put sp-Obscuring Mist condition on obj
	spell_obj_partsys_id = game.particles( 'sp-Obscuring Mist', spell_obj )
	spell_obj.condition_add_with_args( 'sp-Obscuring Mist', spell.id, spell.duration, 0, spell_obj_partsys_id )

	
	#########################
	# Added by Sitra Achara	#
	#########################

	spell_obj.obj_set_int( obj_f_secretdoor_dc, 333 + (1<<15)   ) 
	# Mark it as an "obscuring mist" object. 
	# 1<<15 - marks it as "active"
	# bits 16 and onward - random ID number

	activeList = Co8PersistentData.getData(OBSCURING_MIST_KEY)
	if isNone(activeList): activeList = []
	activeList.append([spell.id, derefHandle(spell_obj)])
	Co8PersistentData.setData(OBSCURING_MIST_KEY, activeList)

	#########################
	# End of Section		#
	#########################

	#spell_obj.condition_add_arg_x( 3, spell_obj_partsys_id )
	#objectevent_id = spell_obj.condition_get_arg_x( 2 )

def OnBeginRound( spell ):
	print "Obscuring Mist OnBeginRound"

def OnEndSpellCast( spell ):
	print "Obscuring Mist OnEndSpellCast"

	activeList = Co8PersistentData.getData(OBSCURING_MIST_KEY)
	if isNone(activeList):
		print "ERROR! Active Obscuring Mist spell without activeList!"
		return

	for entry in activeList:
		spellID, target = entry
		targetObj = refHandle(target)
		if spellID == spell.id:
			aaa = targetObj.obj_get_int( obj_f_secretdoor_dc )
			aaa &= ~(1<<15)
			targetObj.obj_set_int( obj_f_secretdoor_dc, aaa )
			activeList.remove(entry)
			#no more active spells
			if len(activeList) == 0:
				Co8PersistentData.removeData(OBSCURING_MIST_KEY)
				break
    
                	Co8PersistentData.setData(OBSCURING_MIST_KEY, activeList)
			break




def OnAreaOfEffectHit( spell ):
	print "Obscuring Mist OnAreaOfEffectHit"

def OnSpellStruck( spell ):
	print "Obscuring Mist OnSpellStruck"