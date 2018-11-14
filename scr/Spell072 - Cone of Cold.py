from toee import *

def OnBeginSpellCast( spell ):
	print "Cone of Cold OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Cone of Cold OnSpellEffect"

	remove_list = []

	dam = dice_new( '1d6' )
	dam.number = min( 15, spell.caster_level )
	if game.global_vars[451] & 2**1 != 0:
		if game.leader.map == 5083:   ## Fire node - water spells do 1/2 damage
			dam.number = dam.number / 2
		elif game.leader.map == 5084: ## Water node - water spells do X2 damage
			dam.number = dam.number * 2

	game.particles( 'sp-Cone of Cold', spell.caster )

	npc = spell.caster


	#### Caster is NOT in game party
	if npc.type != obj_t_pc and npc.leader_get() == OBJ_HANDLE_NULL:
#		range = 25 + 5 * int(spell.caster_level/2)
		range = 60
		target_list = list(game.obj_list_cone( spell.caster, OLC_CRITTERS, range, -30, 60 ))
		target_list.remove(spell.caster)
		for obj in target_list:
			if obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_COLD, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
				# saving throw successful
				obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
			else:
				# saving throw unsuccessful
				obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

	#### Caster is in game party
	if npc.type == obj_t_pc or npc.leader_get() != OBJ_HANDLE_NULL:

		# get all targets in a 25ft + 2ft/level cone (60')
		for target_item in spell.target_list:

			if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_COLD, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ):
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Cone of Cold OnBeginRound"

def OnEndSpellCast( spell ):
	print "Cone of Cold OnEndSpellCast"