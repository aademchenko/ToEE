from toee import *

def OnBeginSpellCast( spell ):
	print "Sleet Storm OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Sleet Storm OnSpellEffect"

#	spell.duration = 1 * spell.caster_level

	npc = spell.caster			##  added so NPC's can cast Sleet Storm
	if npc.name == 8091:			##  added so NPC's can cast Sleet Storm
		spell.duration = 1		##  added so NPC's can cast Sleet Storm


	# spawn one Sleet Storm scenery object
#	sleet_storm_obj = game.obj_create( OBJECT_SPELL_GENERIC, spell.target_loc )

	# add to d20initiative
#	caster_init_value = spell.caster.get_initiative()
#	sleet_storm_obj.d20_status_init()
#	sleet_storm_obj.set_initiative( caster_init_value )


	# put sp-Sleet Storm condition on obj
#	sleet_storm_partsys_id = game.particles( 'sp-Sleet Storm', sleet_storm_obj )
#	sleet_storm_obj.condition_add_with_args( 'sp-Sleet Storm', spell.id, spell.duration, 0, sleet_storm_partsys_id )
#	sleet_storm_obj.condition_add_with_args( 'prone', spell.id, spell.duration, 0, sleet_storm_partsys_id )

	#sleet_storm_obj.condition_add_arg_x( 3, sleet_storm_partsys_id )
	#objectevent_id = sleet_storm_obj.condition_get_arg_x( 2 )


	remove_list = []

	spell.duration = 1
	dam = dice_new( '2d8' )

	game.pfx_call_lightning( spell.target_loc, spell.target_loc_off_x, spell.target_loc_off_y, spell.target_loc_off_z )

#	game.particles( 'sp-Call Lightning', spell.target_loc )

	for target_item in spell.target_list:

		armor_obj = target_item.obj.item_worn_at( item_wear_armor )

		if (armor_obj != OBJ_HANDLE_NULL) and (armor_obj.obj_get_int( obj_f_material ) == mat_metal):
			# wearing metal armor
			target_item.obj.spell_damage( spell.caster, D20DT_COLD, dam, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
#			target_item.obj.condition_add_with_args( 'sp-Chill Metal', spell.id, spell.duration, 0 )
#			target_item.partsys_id = game.particles( 'sp-Chill Metal', target_item.obj )
			game.particles( 'sp-Shocking Grasp', target_item.obj )

		if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Reflex, D20STD_F_NONE, spell.caster, spell.id ):
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

		else:
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			target_item.obj.condition_add_with_args( 'prone', 0, 0)


	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )


def OnBeginRound( spell ):
	print "Sleet Storm OnBeginRound"

def OnEndSpellCast( spell ):
	print "Sleet Storm OnEndSpellCast"

def OnAreaOfEffectHit( spell ):
	print "Sleet Storm OnAreaOfEffectHit"

def OnSpellStruck( spell ):
	print "Sleet Storm OnSpellStruck"