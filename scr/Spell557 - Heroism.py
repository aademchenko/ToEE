from toee import *

def OnBeginSpellCast( spell ):
	print "Heroism OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Heroism OnSpellEffect"

	spell.duration = 100 * spell.caster_level
	target_item = spell.target_list[0]

	npc = spell.caster			##  added so NPC's can pre-buff
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active():
		spell.duration = 2000 * spell.caster_level

	if target_item.obj.is_friendly( spell.caster ):

		target_item.obj.condition_add_with_args( 'sp-Heroism', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Heroism', target_item.obj )

	elif not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

		# saving throw unsuccesful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		target_item.obj.condition_add_with_args( 'sp-Heroism', spell.id, spell.duration, 0 )
		target_item.partsys_id = game.particles( 'sp-Heroism', target_item.obj )

	else:

		# saving throw successful
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Heroism OnBeginRound"

def OnEndSpellCast( spell ):
	print "Heroism OnEndSpellCast"