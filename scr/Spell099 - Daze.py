from toee import *

def OnBeginSpellCast( spell ):
	print "Daze OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Daze OnSpellEffect"

	spell.duration = 1

	target = spell.target_list[0]

	if target.obj.is_category_type( mc_type_humanoid ):

		if target.obj.hit_dice_num < 5:

			# allow Will saving throw to negate
			if target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
		
				# saving throw successful
				target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
		
				game.particles( 'Fizzle', target.obj )
				spell.target_list.remove_target( target.obj )
			else:
		
				# saving throw unsuccessful
				target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
		
				# HTN - apply condition DAZED
				target.obj.condition_add_with_args( 'sp-Daze', spell.id, spell.duration, 0 )
				target.partsys_id = game.particles( 'sp-Daze', target.obj )

	else:

		spell.target_list.remove_target( target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Daze OnBeginRound"

def OnEndSpellCast( spell ):
	print "Daze OnEndSpellCast"