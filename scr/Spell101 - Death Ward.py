from toee import *
from Co8 import *

SPELL_OBJ = 6400

def OnBeginSpellCast( spell ):
	print "Death Ward OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def do_particles( target ):
	part_str = 'sp-Death Ward'

	if target.obj.get_size <= STAT_SIZE_MEDIUM:
		part_str = 'sp-Death Ward-MED'
	elif target.obj.get_size == STAT_SIZE_LARGE:
		part_str = 'sp-Death Ward-LARGE'
	else:
		part_str = 'sp-Death Ward-HUGE'

	target.partsys_id = game.particles( part_str, target.obj )

def OnSpellEffect ( spell ):
	print "Death Ward OnSpellEffect"

#	Dar's level check no longer needed thanks to Spellslinger's dll fix
#	if spell.caster_class == 13: #added to check for proper paladin slot level (darmagon)
#		if spell.spell_level < 4:
#			spell.caster.float_mesfile_line('mes\\spell.mes', 16008)
#			return

	spell.duration = 10 * spell.caster_level

	npc = spell.caster			##  added so NPC's can pre-buff
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active():
		spell.duration = 2000 * spell.caster_level

	target = spell.target_list[0]

	if find_spell_obj_with_flag( target.obj, SPELL_OBJ,
				     OSF_IS_DEATH_WARD ) == OBJ_HANDLE_NULL:
		spell_obj = game.obj_create( SPELL_OBJ, target.obj.location )
		spell_obj.item_flag_set( OIF_NO_DROP )
		spell_obj.item_flag_set( OIF_NO_LOOT )
		set_spell_flag( spell_obj, OSF_IS_DEATH_WARD )

		spell_obj.item_condition_add_with_args(
			'Monster Energy Immunity', D20DT_NEGATIVE_ENERGY, 0)

		target.obj.item_get( spell_obj )

		target.obj.condition_add_with_args( 'sp-Death Ward',
						    spell.id,
						    spell.duration, 0 )
		do_particles( target )

		# This is evil, but we need to remember who the spell was
		# cast on, and the target_list gets blown away.
		spell.caster = target.obj
	else:
		target.obj.float_mesfile_line( 'mes\\spell.mes', 16007 )
		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_obj( target.obj )
		spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Death Ward OnBeginRound"

def OnEndSpellCast( spell ):
	print "Death Ward OnEndSpellCast"

	destroy_spell_obj_with_flag( spell.caster, SPELL_OBJ,
				     OSF_IS_DEATH_WARD )
