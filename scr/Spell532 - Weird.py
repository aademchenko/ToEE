from toee import *
from utilities import * 

def OnBeginSpellCast( spell ):
	print "Weird OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-illusion-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Weird OnSpellEffect"
	remove_list = []
	dice = dice_new( "3d6" )

	for target in spell.target_list:
		remove_list.append(target.obj)

		game.particles( 'sp-Phantasmal Killer', target.obj )

		# will save to negate, otherwise fort save to avoid death
		if target.obj.saving_throw_spell( spell.dc, D20_Save_Will, D20STD_F_NONE, spell.caster, spell.id ):
			# saving throw successful
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			game.particles( 'Fizzle', target.obj )

		elif target.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_SPELL_DESCRIPTOR_FEAR, spell.caster, spell.id ):

			# fort save success, damage 3d6
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

			# saving throw unsuccesful, damage target, full damage
			target.obj.spell_damage( spell.caster, D20DT_UNSPECIFIED, dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
		else:

			# fort save failure, kill
			target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

			# kill target
			# So you'll get awarded XP for the kill
			if not target.obj in game.leader.group_list():
				target.obj.damage( game.leader , D20DT_UNSPECIFIED, dice_new( "1d1" ) )
			target.obj.critter_kill()

	spell.target_list.remove_list( remove_list )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Weird OnBeginRound"

def OnEndSpellCast( spell ):
	print "Weird OnEndSpellCast"