from toee import *

def OnBeginSpellCast( spell ):
	print "Flare OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-evocation-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Flare OnSpellEffect"

	spell.duration = 10

	target = spell.target_list[0]

	# sightless/blind creatures are unaffected
	if target.obj.d20_query( Q_Critter_Is_Blinded ) == 0:

		# allow Fortitude saving throw to negate
		if target.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
	
			# saving throw successful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )
	
			game.particles( 'Fizzle', target.obj )
			spell.target_list.remove_target( target.obj )

		else:
	
			# saving throw unsuccessful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )
	
			target.obj.condition_add_with_args( 'sp-Flare', spell.id, spell.duration, 0 )
			target.partsys_id = game.particles( 'sp-Flare', target.obj )

	else:

		# target is blind, unaffected
		game.particles( 'Fizzle', target.obj )
		spell.target_list.remove_target( target.obj )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Flare OnBeginRound"

def OnEndSpellCast( spell ):
	print "Flare OnEndSpellCast"