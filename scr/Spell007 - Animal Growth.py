from toee import *
from utilities import  * 

def OnBeginSpellCast( spell ):
	print "Animal Growth OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-transmutation-conjure", spell.caster )

def	OnSpellEffect ( spell ):
	print "Animal Growth OnSpellEffect"

#	Dar's check for ranger caster level no longer needed thanks to Spellslinger's dll hack
#	if spell.caster_class == 14:
#		if spell.spell_level < 4:#added to check for proper ranger slot level (darmagon)
#			spell.caster.float_mesfile_line('mes\\spell.mes', 16008)
#			spell.spell_end(spell.id)
#			return
	remove_list = []

	spell.duration = 10 * spell.caster_level

	for target_item in spell.target_list:

		if (target_item.obj.is_category_type( mc_type_animal ) == 1):

			if target_item.obj.is_friendly( spell.caster ):

				target_item.obj.condition_add_with_args( 'sp-Animal Growth', spell.id, spell.duration, 0 )
				target_item.partsys_id = game.particles( 'sp-Animal Growth', target_item.obj )

			elif not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
	
				# saving throw unsuccessful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

				target_item.obj.condition_add_with_args( 'sp-Animal Growth', spell.id, spell.duration, 0 )
				target_item.partsys_id = game.particles( 'sp-Animal Growth', target_item.obj )
	
			else:
	
				# saving throw successful
				target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

				game.particles( 'Fizzle', target_item.obj )
				remove_list.append( target_item.obj )

		else:
			# not an animal
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30000 )
			target_item.obj.float_mesfile_line( 'mes\\spell.mes', 31002 )

			game.particles( 'Fizzle', target_item.obj )
			remove_list.append( target_item.obj )

	spell.target_list.remove_list( remove_list )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Animal Growth OnBeginRound"

def OnEndSpellCast( spell ):
	print "Animal Growth OnEndSpellCast"