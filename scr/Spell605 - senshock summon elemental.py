from toee import *

def OnBeginSpellCast( spell ):
	print "senshock summon elemental OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "senshock summon elemental OnSpellEffect"

	spell.duration = 50

	# what elementals will we get?
	dice = dice_new( '1d4' )
	proto = dice.roll()

	# set the proto_id for this monster 
	if proto == 1:
#		proto_id = 14292
		proto_id = 14624
	elif proto == 2:
#		proto_id = 14296
		proto_id = 14625
	elif proto == 3:
#		proto_id = 14298
		proto_id = 14626
	else:
#		proto_id = 14302
		proto_id = 14627

	# create monster, monster should be added to target_list
	# monster should disappear when duration is over, apply "TIMED_DISAPPEAR" condition happens auto now...
	# just be sure to set the spell.duration
	spell.summon_monsters( 1, proto_id )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "senshock summon elemental OnBeginRound"

def OnEndSpellCast( spell ):
	print "senshock summon elemental OnEndSpellCast"