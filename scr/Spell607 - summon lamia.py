from toee import *

def OnBeginSpellCast( spell ):
	print "summon lamia OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "summon lamia OnSpellEffect"

	spell.duration = 6

	# get the proto_id for this monster 
	proto_id = 14428

	# create monster, monster should be added to target_list
	# monster should disappear when duration is over, apply "TIMED_DISAPPEAR" condition happens auto now...
	# just be sure to set the spell.duration
	spell.summon_monsters( 1, proto_id )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "summon lamia OnBeginRound"

def OnEndSpellCast( spell ):
	print "summon lamia OnEndSpellCast"