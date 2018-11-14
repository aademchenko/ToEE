from toee import *

def OnBeginSpellCast( spell ):
	print "Power Word Kill OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-enchantment-conjure", spell.caster )

def OnSpellEffect ( spell ):
	print "Power Word Kill OnSpellEffect"

	target = spell.target_list[0]

	# If target has over 100 hit points, spell fails
	if target.obj.stat_level_get( stat_hp_current ) > 100:
		target.obj.float_mesfile_line( 'mes\\spell.mes', 32000 )
		game.particles( 'Fizzle', target.obj )

	# Otherwise, the target dies. Simple.
	else:
		# So you'll get awarded XP for the kill
		if not target.obj in game.leader.group_list():
			target.obj.damage( game.leader , D20DT_UNSPECIFIED, dice_new( "1d1" ) )
		target.obj.critter_kill_by_effect()

	spell.target_list.remove_target( target.obj )
	spell.spell_end(spell.id)

def OnBeginRound( spell ):
	print "Power Word Kill OnBeginRound"

def OnEndSpellCast( spell ):
	print "Power Word Kill OnEndSpellCast"
