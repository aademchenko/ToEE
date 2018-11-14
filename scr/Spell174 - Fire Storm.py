from toee import *
from utilities import *

def OnBeginSpellCast( spell ):
	print "Fire Storm OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Fire Storm OnSpellEffect"

	remove_list = []
	damage_list = []

	dam = dice_new( '1d6' )
	dam.number = min( 20, spell.caster_level )

	xx,yy = location_to_axis(spell.caster.location) ## caster is in chamber
	if game.leader.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
	# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
		game.particles( 'swirled gas', spell.caster )
		spell.caster.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
		game.sound(7581,1)
		game.sound(7581,1)
		spell.spell_end( spell.id )
		return

	for target_item in spell.target_list:
		xx,yy = location_to_axis(target_item.obj.location) # target in chamber
		if game.leader.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
		# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
			tro = game.obj_create(14070, target_item.obj.location)
			game.particles( 'swirled gas', target_item.obj.location )
			# spell.caster.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
			tro.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1)
			tro.destroy()
			game.sound(7581,1)
			game.sound(7581,1)
			remove_list.append( target_item.obj )
			continue

		else:
			# create a rectangle around target for two 10 x 10 ft. cubes (10 x 20 ft. area of effect)
			target_xx,target_yy = location_to_axis(target_item.obj.location)

			# generate location of the rectangle (centered on the target) and randomize the placement of it (since you can not place it)
			a = game.random_range(1,2)
			b = game.random_range(1,2)
			if a == 1:
				targetX = 5
				if b == 1:
					targetY = 7
				else:
					targetY = 10
			else:
				targetY = 5
				if b == 1:
					targetX = 7
				else:
					targetX = 10

			game.particles( 'sp-Flame Strike', location_from_axis(target_xx - int(targetX / 2), target_yy - int(targetY / 2)) )
			game.particles( 'sp-Flame Strike', location_from_axis(target_xx + int(targetX / 2), target_yy + int(targetY / 2)) )

			# create damage list
			for critter in game.obj_list_vicinity(target_item.obj.location, OLC_CRITTERS):
				xx,yy = location_to_axis(critter.location)
				if ( xx >= (target_xx - targetX) and xx <= (target_xx + targetX) ) and ( yy >= (target_yy - targetY) and yy <= (target_yy + targetY) ):
					if critter.map == 5067 and ( xx >= 521 and xx <= 555 ) and ( yy >= 560 and yy <= 610):
						# Water Temple Pool Enchantment prevents fire spells from working inside the chamber, according to the module -SA
						critter.float_mesfile_line( 'mes\\skill_ui.mes', 2000 , 1 )
						game.particles( 'swirled gas', critter )
						game.sound(7581,1)
						game.sound(7581,1)
						continue
					else:
						if critter not in damage_list:
							damage_list.append( critter )

		remove_list.append( target_item.obj )

	# deal damage
	for damage_target in damage_list:
		if damage_target.d20_query(Q_Dead) == 0:
			game.particles( 'hit-FIRE-burst', damage_target )
			if damage_target.reflex_save_and_damage( spell.caster, spell.dc, D20_Save_Reduction_Half, D20STD_F_NONE, dam, D20DT_FIRE, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id ):
				# saving throw successful
				damage_target.float_mesfile_line( 'mes\\spell.mes', 30001 )
			else:
				# saving throw unsuccessful
				damage_target.float_mesfile_line( 'mes\\spell.mes', 30002 )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Fire Storm OnBeginRound"

def OnEndSpellCast( spell ):
	print "Fire Storm OnEndSpellCast"