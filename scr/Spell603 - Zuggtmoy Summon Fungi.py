from toee import *

def OnBeginSpellCast( spell ):
	print "Zuggtmoy Summon Fungi OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Zuggtmoy Summon Fungi OnSpellEffect"

	# this needs to be in every summon spell script!
	spell.duration = 1 * spell.caster_level

	# how many monsters will there be?
	dice1 = dice_new( '1d3' )
	num_summoned = dice1.roll() + 1

	# set the proto_id for basidirond 
	monster_proto_id = 14281

	i = 0
	while i < num_summoned:
		# create monster, monster should be added to target_list
		spell.summon_monsters( 1, monster_proto_id )
		i = i+1

	# how many monsters will there be?
	dice2 = dice_new( '1d3' )
	num_summoned = dice2.roll() + 1

	# set the proto_id for basidirond 
	monster_proto_id = 14284

	j = 0
	while j < num_summoned:
		# create monster, monster should be added to target_list
		spell.summon_monsters( 1, monster_proto_id )
		j = j+1

	# how many monsters will there be?
	dice3 = dice_new( '1d3' )
	num_summoned = dice3.roll() + 1

	# set the proto_id for basidirond 
	monster_proto_id = 14283

	k = 0
	while k < num_summoned:
		# create monster, monster should be added to target_list
		spell.summon_monsters( 1, monster_proto_id )
		k = k+1

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Zuggtmoy Summon Fungi OnBeginRound"

def OnEndSpellCast( spell ):
	print "Zuggtmoy Summon Fungi OnEndSpellCast"