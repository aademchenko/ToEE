from toee import *

def OnBeginSpellCast( spell ):
	print "See Invisibility OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-divination-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "See Invisibility OnSpellEffect"

	spell.duration = 100 * spell.caster_level
	
	npc = spell.caster			##  added so NPC's can pre-buff
	
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active():
		spell.duration = 2000 * spell.caster_level
	if npc.name == 14958: #nightwalker 14958
		spell.duration = 20000
		
	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'sp-See Invisibility', spell.id, spell.duration, 0 )
	target.partsys_id = game.particles( 'sp-See Invisibility', spell.caster )

def OnBeginRound( spell ):
	print "See Invisibility OnBeginRound"

def OnEndSpellCast( spell ):
	print "See Invisibility OnEndSpellCast"