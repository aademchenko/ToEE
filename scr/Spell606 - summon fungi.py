from toee import *

def OnBeginSpellCast( spell ):
	print "summon fungi OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "summon fungi OnSpellEffect"

	spell.duration = 5

	# what fungi will we get?
	dice = dice_new( '1d4' )
	proto = dice.roll()

	# set the proto_id for this monster 
	if proto == 1:
		proto_id = 14281
	elif proto == 2:
		proto_id = 14284
	elif proto == 3:
		proto_id = 14283
	else:
		proto_id = 14277

	# monster should disappear when duration is over, apply "TIMED_DISAPPEAR" condition
	# spell.target_list[0].condition_add_with_args( 'sp-Summoned', spell.id, spell.duration, 0 )
	# Think i am gonna let the creature be there indefinately
	spell.summon_monsters( 1, proto_id )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "summon fungi OnBeginRound"

def OnEndSpellCast( spell ):
	print "summon fungi OnEndSpellCast"