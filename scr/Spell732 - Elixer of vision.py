from toee import *

def OnBeginSpellCast( spell ):
	print "Elixir of vision OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level

def	OnSpellEffect( spell ):
	print "Elixir of vision OnSpellEffect"

	target = spell.target_list[0]

	target.obj.condition_add_with_args( 'Elixer Timed Skill Bonus', 2, 0, 0 )

	#spell.target_list.remove_target( target.obj )
	#spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Elixir of vision OnBeginRound"

def OnEndSpellCast( spell ):
	print "Elixir of vision OnEndSpellCast"