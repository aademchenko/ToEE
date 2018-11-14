from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Freedom of Movement OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Freedom of Movement OnSpellEffect"

	if spell.caster_class == 14:
		if spell.spell_level < 4:	# added to check for proper ranger slot level (darmagon)
			spell.caster.float_mesfile_line( 'mes\\spell.mes', 16008 )
			return

	spell.duration = 100 * spell.caster_level

	npc = spell.caster			## added so NPC's can pre-buff
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active():
		spell.duration = 2000 * spell.caster_level

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-Freedom of Movement', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-Freedom of Movement', target.obj )

def OnBeginRound( spell ):
	print "Freedom of Movement OnBeginRound"

def OnEndSpellCast( spell ):
	print "Freedom of Movement OnEndSpellCast"