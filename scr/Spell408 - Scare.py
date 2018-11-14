from toee import *

def OnBeginSpellCast( spell ):
	print "Scare OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Scare OnSpellEffect"

	remove_list = []

	spell.duration = spell.caster_level

	for target_item in spell.target_list:
		# check for vermin
		if target_item.obj.is_category_type(mc_type_vermin):
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30019 )
			target_item.obj.float_mesfile_line( 'mes\\bonus.mes', 319 )
			remove_list.append( target_item.obj )

		# check target HD
		elif (target_item.obj.hit_dice_num < 6):

			# allow Will saving throw to negate
			if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
				# target is SHAKEN
				target_item.obj.condition_add_with_args( 'sp-Cause Fear', spell.id, 1, 1 )
				target_item.partsys_id = game.particles( 'sp-Scare', target_item.obj )

			else:
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
				# target is FRIGHTENED
				target_item.obj.condition_add_with_args( 'sp-Cause Fear', spell.id, spell.duration, 0 )
				target_item.partsys_id = game.particles( 'sp-Scare', target_item.obj )

		else:
			# target HD is 6 or more
			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Scare OnBeginRound"

def OnEndSpellCast( spell ):
	print "Scare OnEndSpellCast"