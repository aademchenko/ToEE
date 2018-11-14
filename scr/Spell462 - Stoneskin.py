from toee import *

def OnBeginSpellCast( spell ):
	print "Stoneskin OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Stoneskin OnSpellEffect"

	spell.duration = 100 * spell.caster_level
	damage_max = 10 * min( 15, spell.caster_level )

	npc = spell.caster			##  added so NPC's can pre-buff
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active():
		spell.duration = 2000 * spell.caster_level

	npc = spell.caster			##  added so NPC's can use wand/potion/scroll
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and spell.duration <= 0:
		spell.caster_level = 10
		damage_max = 100
		spell.duration = 1000

	target = spell.target_list[0]

	if npc.name == 14609:
		spell.caster_level = 8
	if npc.name == 14601:
		spell.caster_level = 4
	if npc.name == 14241:
		damage_max = 60

	partsys_id = game.particles( 'sp-Stoneskin', target.obj )

	if target.obj.is_friendly( spell.caster ):

		target.obj.condition_add_with_args( 'sp-Stoneskin', spell.id, spell.duration, partsys_id, damage_max )
		#target.obj.condition_add( 'sp-Stoneskin' )
		#target.obj.condition_add_arg_spell_id( spell.id )
		#target.obj.condition_add_arg_duration( spell.duration )
		#target.obj.condition_add_arg_partsys_id( partsys_id )
		#target.obj.condition_add_arg_x( 3, damage_max )

	elif not target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

		# saving throw unsuccessful
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		target.obj.condition_add_with_args( 'sp-Stoneskin', spell.id, spell.duration, partsys_id, damage_max )
		#target.obj.condition_add( 'sp-Stoneskin' )
		#target.obj.condition_add_arg_spell_id( spell.id )
		#target.obj.condition_add_arg_duration( spell.duration )
		#target.obj.condition_add_arg_partsys_id( partsys_id )
		#target.obj.condition_add_arg_x( 3, damage_max )

	else:

		# saving throw successful
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_target( target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Stoneskin OnBeginRound"

def OnEndSpellCast( spell ):
	print "Stoneskin OnEndSpellCast"