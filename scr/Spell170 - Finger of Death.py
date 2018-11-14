from toee import *
from utilities import  * 

def OnBeginSpellCast( spell ):
	print "Finger of Death OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Finger of Death OnSpellEffect"

	damage_dice = dice_new( "3d6" )
	damage_dice.bonus = min( 25, spell.caster.stat_level_get( spell.caster_class ) )

	target = spell.target_list[0]

	game.particles( 'sp-Slay Living', target.obj )

	# damage target
	if target.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

		# saving throw succesful, damage target
		target.obj.spell_damage( spell.caster, D20DT_UNSPECIFIED, damage_dice, D20DAP_UNSPECIFIED, D20A_CAST_SPELL, spell.id )
	else:
		target.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		# saving throw unsuccesful, kill target
		# So you'll get awarded XP for the kill
		if not target.obj in game.leader.group_list():
			target.obj.damage( game.leader , D20DT_UNSPECIFIED, dice_new( "1d1" ) )
		target.obj.critter_kill_by_effect()

	spell.target_list.remove_target( target.obj )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Finger of Death OnBeginRound"

def OnEndSpellCast( spell ):
	print "Finger of Death OnEndSpellCast"