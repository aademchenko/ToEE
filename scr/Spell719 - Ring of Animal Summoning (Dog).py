from toee import *

#I now serve the Bag of Tricks

def OnBeginSpellCast( spell ):
	print "Ring of Animal Summoning (Dog) OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Summon Natures Ally II OnSpellEffect"

	spell.duration = 100
	roll = game.random_range(1, 100)

	if roll < 15:
		monster_proto_id = 14050
	elif roll < 30:
		monster_proto_id = 14051
	elif roll < 45:
		monster_proto_id = 14053
	elif roll < 60:
		monster_proto_id = 14052
	elif roll < 75:
		monster_proto_id = 14047
	elif roll < 90:
		monster_proto_id = 14090
	else:
		monster_proto_id = 14375

	# special effects
	game.particles( 'sp-Summon Natures Ally II', spell.target_loc )
	spell.summon_monsters( 1, monster_proto_id )

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Ring of Animal Summoning (Dog) OnBeginRound"

def OnEndSpellCast( spell ):
	print "Ring of Animal Summoning (Dog) OnEndSpellCast"