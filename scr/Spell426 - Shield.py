from toee import *

def OnBeginSpellCast( spell ):
	print "Shield OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-abjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Shield OnSpellEffect"

	spell.duration = 10 * spell.caster_level

	npc = spell.caster			##  added so NPC's can pre-buff
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active():
		spell.duration = 30 * spell.caster_level

	target_item = spell.target_list[0]

	target_item.obj.condition_add_with_args( 'sp-Shield', spell.id, spell.duration, 4 )
	target_item.partsys_id = game.particles( 'sp-Shield', target_item.obj )

def OnBeginRound( spell ):
	print "Shield OnBeginRound"

def OnEndSpellCast( spell ):
	print "Shield OnEndSpellCast"