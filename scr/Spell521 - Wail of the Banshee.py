from toee import *

def OnBeginSpellCast( spell ):
	print "Wail of the Banshee OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

	# Sorts the targets by distance, so closest are affected first
	spell.spell_target_list_sort( SORT_TARGET_LIST_BY_DIST, SORT_TARGET_LIST_ORDER_ASCENDING )
	print "target_list sorted by dist from target_Loc (least to greatest): ", spell.target_list

def OnSpellEffect ( spell ):
	print "Wail of the Banshee OnSpellEffect"

	remove_list = []

	banshee_targets = spell.caster_level

	game.particles( 'sp-Shout', spell.caster )
	game.particles( 'sp-Dispel Magic - Area', spell.target_loc )

	for target_item in spell.target_list:

		if banshee_targets > 0:

			# make sure target is alive
			if target_item.obj.is_category_type( mc_type_construct ) or target_item.obj.is_category_type( mc_type_undead ):
				# not alive
				game.particles( 'Fizzle', target_item.obj )

			else:
				# allow Fortitude saving throw to negate
				if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
					# saving throw successful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
					game.particles( 'Fizzle', target_item.obj )

				else:
					# saving throw unsuccessful
					target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
	
					# kill target
					game.particles( 'sp-Shout-Hit', target_item.obj )
					game.particles( 'sp-Death Knell-Target', target_item.obj )
					# So you'll get awarded XP for the kill
					if not target_item.obj in game.leader.group_list():
						target_item.obj.damage( game.leader , D20DT_UNSPECIFIED, dice_new( "1d1" ) )
					target_item.obj.critter_kill()

				banshee_targets = banshee_targets - 1

		remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Wail of the Banshee OnBeginRound"

def OnEndSpellCast( spell ):
	print "Wail of the Banshee OnEndSpellCast"