from toee import *

def OnBeginSpellCast( spell ):
	print "Death Gaze OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect( spell ):
	print "Death Gaze OnSpellEffect"

	spell.dc = 15

	target = spell.target_list[0]

	game.particles( 'sp-Slay Living', target.obj )

	# damage target
	if target.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

	else:
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		# saving throw unsuccesful, kill target
		target.obj.critter_kill_by_effect()

	spell.target_list.remove_target( target.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Death Gaze OnBeginRound"

def OnEndSpellCast( spell ):
	print "Death Gaze OnEndSpellCast"