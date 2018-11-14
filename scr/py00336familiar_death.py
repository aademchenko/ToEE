from toee import *
from combat_standard_routines import *
from __main__ import game
from utilities import *


familiar_table = {
12045: 14900,
12046: 14901,
12047: 14902,
12048: 14903,
12049: 14904,
12050: 14905,
12051: 14906,
12052: 14907,
12053: 14908,
12054: 14909
}

def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT

def san_dying( attachee, triggerer ):
	game.timevent_add( RemoveDead, ( game.party[0], attachee ), 86400000) # remove the familiar from the party in 24 hours
	# identify familiar dying and match to familiar inventory icon
	familiar_proto = FindFamiliarInvType( attachee )
	if ( familiar_proto == OBJ_HANDLE_NULL ):
		return SKIP_DEFAULT # not a valid familiar type
	
	# search for familiar inventory icon in all PCs' inventory
	for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
		inv_familiar = obj.item_find_by_proto( familiar_proto )
		if ( inv_familiar != OBJ_HANDLE_NULL ):
			# check for correct ID number
			if ( get_ID( inv_familiar ) == get_ID( attachee ) ):
				# destroys familiar in owner's inventory and removes experience from owner
				inv_familiar.destroy()
				curxp = obj.stat_level_get( stat_experience )
				ownerlevel = GetLevel( obj )
				if ( obj.saving_throw( 15, D20_Save_Fortitude, D20STD_F_NONE, attachee ) == 0 ):
					xploss = ownerlevel * 200
				else:
					xploss = ownerlevel * 100
				if ( curxp >= xploss ):
					newxp = curxp - xploss
				else:
					newxp = 0
				obj.stat_base_set( stat_experience, newxp )
				return SKIP_DEFAULT
	return RUN_DEFAULT

def FindFamiliarInvType( attachee ):
	for f,p in familiar_table.items():
		if (attachee.name == p):
			return f
	return OBJ_HANDLE_NULL

def get_ID(obj):
	return obj.obj_get_int(obj_f_secretdoor_dc)
	
def clear_ID( obj ):
# Clears embedded ID number from mobile object
	obj.obj_set_int( obj_f_secretdoor_dc, 0 )

def GetLevel( npc ):
	level = npc.stat_level_get(stat_level_sorcerer) + npc.stat_level_get(stat_level_wizard)
	return level
	
def StowFamiliar(attachee, pc):

	# identify familiar  and match to familiar inventory icon
	familiar_proto = FindFamiliarInvType( attachee )
	if ( familiar_proto == OBJ_HANDLE_NULL ):
		return SKIP_DEFAULT # not a valid familiar type
	
	# search for familiar inventory icon in all PCs' inventory
	for obj in game.obj_list_vicinity( attachee.location, OLC_CRITTERS ):
		inv_familiar = obj.item_find_by_proto( familiar_proto )
		if ( inv_familiar != OBJ_HANDLE_NULL ):
			# check for correct ID number
			if ( get_ID( inv_familiar ) == get_ID( attachee ) ):
				max_hp = attachee.stat_level_get(stat_hp_max)
				inv_familiar.obj_set_int(obj_f_item_pad_i_1, max_hp)
				curr_hp = attachee.stat_level_get(stat_hp_current)
				inv_familiar.obj_set_int(obj_f_item_pad_i_2, curr_hp)
				pc.follower_remove( attachee )
				attachee.destroy()
				clear_ID( inv_familiar )
				return SKIP_DEFAULT
	return SKIP_DEFAULT
			

def FindMaster( npc ):
# Not actually used in the spell, but could be handy in the future.  Returns the character that is the master for a given summoned familiar ( npc )
	for p_master in game.obj_list_vicinity( npc.location, OLC_CRITTERS ):
		for x,y in familiar_table.items():
			item = p_master.item_find_by_proto( x )
			if (item != OBJ_HANDLE_NULL):
				if ( get_ID(item) == get_ID( npc ) ):
					return p_master
	return OBJ_HANDLE_NULL

def RemoveDead(npc, critter):
	if critter.stat_level_get(stat_hp_current) <= -10:
		npc.follower_remove(critter)
	return