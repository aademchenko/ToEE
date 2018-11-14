from toee import *

def OnBeginSpellCast( spell ):
	print "Poison OnBeginSpellCast"
	print "spell.target_list=", spell.target_list
	print "spell.caster=", spell.caster, " caster.level= ", spell.caster_level
	game.particles( "sp-necromancy-conjure", spell.caster )

def	OnSpellEffect( spell ):
	print "Poison OnSpellEffect"

	# 20 == SPELL_POISON, 10 == 1 minute til secondary damage
	poison_index = 23
	time_to_secondary = 10
	poison_dc = 10 + (spell.caster_level / 2) + game.get_stat_mod( spell.caster.stat_level_get( stat_wisdom ) )
	#print "poison-dc=", poison_dc

	spell.duration = 0
	target_item = spell.target_list[0]

	#if not target_item.obj.saving_throw_spell( spell.dc, D20_Save_Fortitude, D20STD_F_NONE, spell.caster, spell.id ):

		# saving throw unsuccesful
	target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30002 )

		#target_item.obj.condition_add_with_args( 'sp-Poison', spell.id, spell.duration, disease_index )
	target_item.obj.condition_add_with_args( 'Poisoned', poison_index, time_to_secondary, poison_dc )
	target_item.partsys_id = game.particles( 'sp-Poison', target_item.obj )

	#else:

		# saving throw successful
  #		target_item.obj.float_mesfile_line( 'mes\\spell.mes', 30001 )

# 		game.particles( 'Fizzle', target_item.obj )

	spell.target_list.remove_target( target_item.obj )
	spell.spell_end( spell.id )

def OnBeginRound( spell ):
	print "Poison OnBeginRound"

def OnEndSpellCast( spell ):
	print "Poison OnEndSpellCast"