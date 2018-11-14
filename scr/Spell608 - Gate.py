from toee import *

def OnBeginSpellCast( spell ):
	print "Gate OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-conjuration-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "gate OnSpellEffect"

	# this needs to be in every summon spell script!
	spell.duration = 500

	# What Demon will it be?
	dice1 = dice_new( '1d100' )
	what_summoned = dice1.roll()

	if what_summoned > 99:
		# set the  proto_id for Balor
		monster_proto_id = 14286
		num_monsters = 1
	elif what_summoned > 75:
		# set the  proto_id for Glabrezu
		monster_proto_id = 14263
		num_monsters = 1
	elif what_summoned > 50:
		# set the  proto_id for Hezrou
		monster_proto_id = 14259
		dice2 = dice_new( '1d2' );
		num_monsters = dice2.roll();
	else:
		# set the  proto_id for Vrock
		monster_proto_id = 14258
		dice2 = dice_new( '1d3' );
		num_monsters = dice2.roll();


	i = 0
	while i < num_monsters:
		# create monster, monster should be added to target_list
		spell.summon_monsters( 1, monster_proto_id )
		i = i+1

	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Gate OnBeginRound"

def OnEndSpellCast( spell ):
	print "Gate OnEndSpellCast"