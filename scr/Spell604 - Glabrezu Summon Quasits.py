from toee import *

def OnBeginSpellCast( spell ):
	print "Glabrezu Summon Quasits OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Glabrezu Summon Quasits OnSpellEffect"
	
	# this needs to be in every summon spell script!
	spell.duration = 1 * spell.caster_level

	# how many quasits will there be?
	dice = dice_new( '1d4' )
	num_quasits = dice.roll()

	# set the proto_id for this monster 
	quasit_proto_id = 14110

	npc = spell.caster		## Vrock/Hezrou/Glabrezu Guardian can summon 1d10 Quasits
	if npc.name == 14360 or npc.name == 14361 or npc.name == 14359:			
		dice2 = dice_new( '2d3' )
		num_quasits = num_quasits + dice2.roll()

	## Balor Guardian
	if npc.name == 14358:	
		chance = game.random_range(1,100)		
		if chance <= 25:				## Lots of Quasits
			num_quasits = game.random_range(4,10)
		if chance >= 26 and chance <= 50:   ## Lesser Glabrezu
			num_quasits = 1
			quasit_proto_id = 14263
		if chance >= 51 and chance <= 75:   ## Lesser Hezrou
			num_quasits = game.random_range(1,3)
			quasit_proto_id = 14259
		if chance >= 76 and chance <= 100:  ## Lesser Balor
			num_quasits = 1
			quasit_proto_id = 14286

	## Vrock Guardian has 25% chance to summon a lesser Vrock instead of Quasitz
	if npc.name == 14361 and game.random_range(1,100) <= 25:			
		num_quasits = 1
		quasit_proto_id = 14258

	## Hezrou Guardian has 25% chance to summon a lesser Hezrou instead of Quasitz
	if npc.name == 14360: # and game.random_range(1,100) <= 25:			
		num_quasits = 1
		quasit_proto_id = 14259

	## Glabrezu Guardian has 25% chance to summon a lesser Vrock instead of Quasitz
	if npc.name == 14359 and game.random_range(1,100) <= 25:			
		num_quasits = 1
		quasit_proto_id = 14258

	i = 0
	while i < num_quasits:
		# create monster, monster should be added to target_list
		spell.summon_monsters( 1, quasit_proto_id )
		i = i+1

	# monster should disappear when duration is over, apply "TIMED_DISAPPEAR" condition
	# spell.target_list[0].condition_add_with_args( 'sp-Summoned', spell.id, spell.duration, 0 )
	# Think i am gonna let the creature be there indefinately

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Glabrezu Summon Quasits OnBeginRound"

def OnEndSpellCast( spell ):
	print "Glabrezu Summon Quasits OnEndSpellCast"