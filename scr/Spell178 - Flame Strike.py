from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Flame Strike OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Flame Strike OnSpellEffect"

	remove_list = []

	# damage is split between FIRE and DIVINE damage
	dam = dice_new( '1d6' )
	dam.number = min( 15, spell.caster_level )
	dam_over2 = dice_new( "0d0" )
	dam_over2.bonus = dam.roll() / 2

	xx,yy = location_to_axis(spell.caster.location) ## caster is in chamber
	if game.leader.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
	# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
		game.particles( 'swirled gas', spell.caster )
		spell.caster.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
		game.sound(7581,1)
		game.sound(7581,1)
		for target_item in spell.target_list:
			remove_list.append( target_item.obj )
		spell.spell_end( spell.id )

		return

	xx,yy = location_to_axis(spell.target_loc) # center of targeting circle in chamber
	if game.leader.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
	# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
		tro = game.obj_create(14070, spell.target_loc)
		game.particles( 'swirled gas', spell.target_loc )
		spell.caster.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
		tro.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1)
		tro.destroy()
		game.sound(7581,1)
		game.sound(7581,1)
		for target_item in spell.target_list:
			remove_list.append( target_item.obj )
		spell.spell_end( spell.id )
		return


	game.particles( 'sp-Flame Strike', spell.target_loc )


	# get all targets in a 10ft radius

	soundfizzle = 0

	for target_item in spell.target_list:
		xx,yy = location_to_axis(target_item.obj.location) # center of targeting circle in chamber

		if game.leader.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
			# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
			game.particles( 'swirled gas', target_item.obj.location )
			target_item.obj.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1)
			soundfizzle = 1
			spell.target_list.remove_target( target_item.obj )
			remove_list.append( target_item.obj )
			continue

		# do reflex saving throw on FIRE damage, then do damage/save check for DIVINE damage
		if target_item.obj.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam_over2, D20DT_FIRE, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ) > 0:
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			# check for evasion
			if (not target_item.obj.has_feat( feat_evasion )) and (not target_item.obj.has_feat( feat_improved_evasion )):
				# saving throw successful, apply half damage
				target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_MAGIC, dam_over2, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )

		else:
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			if not target_item.obj.has_feat( feat_improved_evasion ):
				# saving throw unsuccessful, apply full damage
				target_item.obj.spell_damage( spell.caster, D20DT_MAGIC, dam_over2, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
			else:
				# saving throw successful, apply half damage because of IMPROVED EVASION
				target_item.obj.spell_damage_with_reduction( spell.caster, D20DT_MAGIC, dam_over2, D20DAP_UNSPECIFIED, DAMAGE_REDUCTION_HALF, D20A_CAST_SPELL, spell.id )

		remove_list.append( target_item.obj )

	if soundfizzle == 1:
		game.sound(7581,1)
		game.sound(7581,1)
	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Flame Strike OnBeginRound"

def OnEndSpellCast( spell ):
	print "Flame Strike OnEndSpellCast"