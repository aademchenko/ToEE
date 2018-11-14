from toee import *

def OnBeginSpellCast( spell ):
	print "Cause Fear OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Cause Fear OnSpellEffect"

	dice = dice_new( '1d4' )
	spell.duration = dice.roll()
	target_item = spell.target_list[0]

	if (target_item.obj.hit_dice_num < 6):
		# allow Will saving throw to negate
		if target_item.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):

			# saving throw successful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			#game.particles( 'Fizzle', target_item.obj )
			#spell.target_list.remove_target( target_item.obj )

			# shaken
			return_val = target_item.obj.condition_add_with_args( 'sp-Cause Fear', spell.id, 1, 1 )
			if return_val == 1:
				target_item.partsys_id = game.particles( 'sp-Cause Fear', target_item.obj )

		else:

			# saving throw unsuccessful
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			# frightened
			return_val = target_item.obj.condition_add_with_args( 'sp-Cause Fear', spell.id, spell.duration, 0 )
			if return_val == 1:
				target_item.partsys_id = game.particles( 'sp-Cause Fear', target_item.obj )

	else:
		# cannot affect HD > 5
		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30003 )

		game.particles( 'Fizzle', target_item.obj )
		spell.target_list.remove_target( target_item.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Cause Fear OnBeginRound"

def OnEndSpellCast( spell ):
	print "Cause Fear OnEndSpellCast"